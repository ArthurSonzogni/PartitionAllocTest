#!/usr/bin/env python3
import subprocess
import os
import re
from settings import START_COMMIT, REPO_DIR
from build_gn import build_gn
from git_utils import get_commits_after
from config_utils import get_configurations
from build_runner import check_commit_and_save_output
from report_generator import update_readme

def parse_row_status(row_line):
    parts = [p.strip() for p in row_line.split('|')]
    if len(parts) < 5:
        return None
    statuses = []
    for p in parts[4:-1]:
        if "🟩" in p:
            statuses.append("🟩")
        elif "🟥" in p:
            statuses.append("🟥")
        else:
            statuses.append("⬜")
    
    commit_hash = None
    match = re.search(r'\./output/[^/]+/([0-9a-f]+)\.log', row_line)
    if match:
        commit_hash = match.group(1)
        
    return {
        "hash": commit_hash,
        "statuses": statuses
    }

def get_latest_commit_status_from_readme():
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        return None
    
    with open(readme_path, "r") as f:
        content = f.read()
    
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if line.startswith("| Email | Date | Title |"):
            if i + 2 < len(lines):
                first_row = lines[i+2]
                if first_row.strip():
                    return parse_row_status(first_row)
    return None

def main():
    """
    Main function to run the build checks and update the README.
    """
    build_gn()
    configurations = get_configurations()
    commits = get_commits_after(START_COMMIT)
    
    old_status = get_latest_commit_status_from_readme()
    print(f"Old latest status: {old_status}")
    
    for commit_hash, _, _, _ in commits:
        for config_name, config_path in configurations:
            check_commit_and_save_output(commit_hash, config_name, config_path)
        subprocess.run(["git", "checkout", "main"], cwd=REPO_DIR, check=True, capture_output=True)

    update_readme(commits, configurations)
    
    new_status = get_latest_commit_status_from_readme()
    print(f"New latest status: {new_status}")
    
    if old_status and new_status:
        old_is_green = all(s == "🟩" for s in old_status["statuses"]) if old_status["statuses"] else False
        old_is_red = any(s == "🟥" for s in old_status["statuses"]) if old_status["statuses"] else False
        
        new_is_green = all(s == "🟩" for s in new_status["statuses"]) if new_status["statuses"] else False
        new_is_red = any(s == "🟥" for s in new_status["statuses"]) if new_status["statuses"] else False
        
        old_state = "GREEN" if old_is_green else ("RED" if old_is_red else "UNKNOWN")
        new_state = "GREEN" if new_is_green else ("RED" if new_is_red else "UNKNOWN")
        
        print(f"State transition: {old_state} -> {new_state}")
        
        if old_state != new_state:
            print("STATE_CHANGED=true")
            if "GITHUB_OUTPUT" in os.environ:
                with open(os.environ["GITHUB_OUTPUT"], "a") as f:
                    f.write("state_changed=true\n")
                    f.write(f"old_state={old_state}\n")
                    f.write(f"new_state={new_state}\n")
                    f.write(f"latest_commit={new_status['hash']}\n")
        else:
            print("STATE_CHANGED=false")
            if "GITHUB_OUTPUT" in os.environ:
                with open(os.environ["GITHUB_OUTPUT"], "a") as f:
                    f.write("state_changed=false\n")
    elif new_status:
        new_is_red = any(s == "🟥" for s in new_status["statuses"]) if new_status["statuses"] else False
        new_state = "RED" if new_is_red else "GREEN"
        print(f"Initial state: {new_state}")
        if new_state == "RED":
            if "GITHUB_OUTPUT" in os.environ:
                with open(os.environ["GITHUB_OUTPUT"], "a") as f:
                    f.write("state_changed=true\n")
                    f.write("old_state=UNKNOWN\n")
                    f.write(f"new_state={new_state}\n")
                    f.write(f"latest_commit={new_status['hash']}\n")

if __name__ == "__main__":
    main()