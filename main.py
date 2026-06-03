#!/usr/bin/env python3
import subprocess
import os
import re
import json
import urllib.request
from settings import START_COMMIT, REPO_DIR, OUTPUT_DIR
from build_gn import build_gn
from git_utils import get_commits_after
from config_utils import get_configurations
from build_runner import check_commit_and_save_output
from report_generator import update_readme, get_build_status_icon

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

def load_json_file(path, default=[]):
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading {path}: {e}")
    return default

def create_github_issue(title, body, assignees=[]):
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not token or not repo:
        print("GITHUB_TOKEN or GITHUB_REPOSITORY not set. Skipping issue creation.")
        return
    
    url = f"https://api.github.com/repos/{repo}/issues"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "Mozilla/5.0"
    }
    data = {
        "title": title,
        "body": body,
        "labels": ["bug", "build-failure"]
    }
    if assignees:
        valid_assignees = [a.replace("@", "").strip() for a in assignees if a]
        valid_assignees = list(set(valid_assignees))
        if "ArthurSonzogni" not in valid_assignees:
            valid_assignees.append("ArthurSonzogni")
        data["assignees"] = valid_assignees
        
    req = urllib.request.Request(url, headers=headers, data=json.dumps(data).encode(), method="POST")
    try:
        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode())
            print(f"Created issue: {res.get('html_url')}")
    except Exception as e:
        print(f"Failed to create issue: {e}")

def close_github_issues(comment_body):
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not token or not repo:
        print("GITHUB_TOKEN or GITHUB_REPOSITORY not set. Skipping issue closure.")
        return
    
    list_url = f"https://api.github.com/repos/{repo}/issues?state=open&labels=build-failure"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "Mozilla/5.0"
    }
    
    req = urllib.request.Request(list_url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            issues = json.loads(response.read().decode())
            
        for issue in issues:
            issue_number = issue.get('number')
            
            # Create comment
            comment_url = f"https://api.github.com/repos/{repo}/issues/{issue_number}/comments"
            comment_data = {"body": comment_body}
            comment_req = urllib.request.Request(comment_url, headers=headers, data=json.dumps(comment_data).encode(), method="POST")
            try:
                with urllib.request.urlopen(comment_req) as _:
                    pass
            except Exception as e:
                print(f"Failed to comment on issue #{issue_number}: {e}")
            
            # Close issue
            close_url = f"https://api.github.com/repos/{repo}/issues/{issue_number}"
            close_data = {"state": "closed", "state_reason": "completed"}
            close_req = urllib.request.Request(close_url, headers=headers, data=json.dumps(close_data).encode(), method="PATCH")
            try:
                with urllib.request.urlopen(close_req) as _:
                    print(f"Closed issue #{issue_number}")
            except Exception as e:
                print(f"Failed to close issue #{issue_number}: {e}")
                
    except Exception as e:
        print(f"Failed to list/process issues for closure: {e}")

def get_mentions(author_email, author_map, always_notify):
    mentions = []
    email_prefix = author_email.split('@')[0]
    
    github_user = author_map.get(email_prefix)
    if github_user:
        mentions.append(f"@{github_user}")
    else:
        mentions.append(author_email)
        
    for user in always_notify:
        if user not in mentions and f"@{user}" not in mentions:
            mentions.append(f"@{user}")
            
    return mentions

def main():
    """
    Main function to run the build checks, update the README, and handle notifications.
    """
    build_gn()
    configurations = get_configurations()
    commits = get_commits_after(START_COMMIT)
    
    author_map = load_json_file("author_map.json", {})
    always_notify = load_json_file("always_notify.json", [])
    
    old_status = get_latest_commit_status_from_readme()
    print(f"Old latest status: {old_status}")
    
    sorted_configurations = sorted(configurations, key=lambda x: x[0])
    
    old_state = "UNKNOWN"
    if old_status and old_status["statuses"]:
        old_is_green = all(s == "🟩" for s in old_status["statuses"])
        old_is_red = any(s == "🟥" for s in old_status["statuses"])
        old_state = "GREEN" if old_is_green else ("RED" if old_is_red else "UNKNOWN")
        
    current_state = old_state
    print(f"Initial state: {current_state}")
    
    transitions = []
    
    for commit_hash, commit_email, commit_date, commit_title in commits:
        for config_name, config_path in sorted_configurations:
            check_commit_and_save_output(commit_hash, config_name, config_path)
        subprocess.run(["git", "checkout", "main"], cwd=REPO_DIR, check=True, capture_output=True)
        
        commit_statuses = []
        for config_name, _ in sorted_configurations:
            log_file = os.path.join(OUTPUT_DIR, config_name, f"{commit_hash}.log")
            commit_statuses.append(get_build_status_icon(log_file))
            
        commit_is_green = all(s == "🟩" for s in commit_statuses) if commit_statuses else False
        commit_is_red = any(s == "🟥" for s in commit_statuses) if commit_statuses else False
        
        commit_state = "GREEN" if commit_is_green else ("RED" if commit_is_red else "UNKNOWN")
        
        if current_state != "UNKNOWN" and commit_state != "UNKNOWN" and current_state != commit_state:
            transitions.append({
                "from": current_state,
                "to": commit_state,
                "commit": commit_hash,
                "author_email": commit_email,
                "title": commit_title
            })
            
        if commit_state != "UNKNOWN":
            current_state = commit_state

    update_readme(commits, configurations)
    
    if transitions:
        print(f"Detected {len(transitions)} transitions:")
        for t in transitions:
            print(f"  {t['from']} -> {t['to']} at {t['commit'][:8]} by {t['author_email']}")
            
        for transition in transitions:
            commit_hash = transition["commit"]
            author_email = transition["author_email"]
            title = transition["title"]
            from_state = transition["from"]
            to_state = transition["to"]
            
            mentions = get_mentions(author_email, author_map, always_notify)
            mentions_str = " ".join(mentions)
            
            if to_state == "RED":
                issue_title = f"🚨 Build Broke at commit {commit_hash[:8]}"
                issue_body = f"""The standalone PartitionAlloc build is now failing.

**Transition:** {from_state} -> {to_state}
**Commit:** https://chromium.googlesource.com/chromium/src/base/allocator/partition_allocator/+/{commit_hash}
**Title:** {title}
**Author:** {author_email}

Cc: {mentions_str}
"""
                assignees = ["ArthurSonzogni"]
                email_prefix = author_email.split('@')[0]
                github_user = author_map.get(email_prefix)
                if github_user:
                    assignees.append(github_user)
                    
                create_github_issue(issue_title, issue_body, assignees)
                
            elif to_state == "GREEN":
                comment_body = f"""The standalone PartitionAlloc build is back to green.

**Transition:** {from_state} -> {to_state}
**Commit:** https://chromium.googlesource.com/chromium/src/base/allocator/partition_allocator/+/{commit_hash}
**Title:** {title}
**Author:** {author_email}

Cc: {mentions_str}
"""
                close_github_issues(comment_body)
    else:
        print("No state transitions detected.")

if __name__ == "__main__":
    main()