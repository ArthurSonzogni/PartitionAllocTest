#!/usr/bin/env python3
import subprocess
from settings import START_COMMIT, REPO_DIR
from build_gn import build_gn
from git_utils import get_commits_after
from config_utils import get_configurations
from build_runner import check_commit_and_save_output
from report_generator import update_readme

def main():
    """
    Main function to run the build checks and update the README.
    """
    build_gn()
    configurations = get_configurations()
    commits = get_commits_after(START_COMMIT)
    
    for commit_hash, _, _, _ in commits:
        for config_name, config_path in configurations:
            check_commit_and_save_output(commit_hash, config_name, config_path)
        subprocess.run(["git", "checkout", "main"], cwd=REPO_DIR, check=True, capture_output=True)

    update_readme(commits, configurations)

if __name__ == "__main__":
    main()