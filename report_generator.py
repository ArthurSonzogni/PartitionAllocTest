import os
from settings import OUTPUT_DIR

def _get_build_status_icon(log_file_path):
    """
    Determines the build status icon based on the content of the log file.
    """
    if not os.path.exists(log_file_path):
        return "⚪"
        
    with open(log_file_path, "r") as f:
        content = f.read()
        if "ERROR" in content or "FAILED" in content:
            return "❌"
        return "✅"

def update_readme(commits, configurations):
    """
    Updates README.md with tables of build results for each configuration.
    """
    readme_path = "README.md"
    
    try:
        with open(readme_path, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []
    
    header_lines = []
    for line in lines:
        if line.strip() == "## Build Results":
            break
        header_lines.append(line)

    full_table = "## Build Results\n\n"
    reversed_commits = list(reversed(commits))

    for config_name, _ in configurations:
        latest_commit_hash = reversed_commits[0][0] if reversed_commits else None
        icon = "⚪"
        if latest_commit_hash:
            log_file = os.path.join(OUTPUT_DIR, config_name, f"{latest_commit_hash}.log")
            icon = _get_build_status_icon(log_file)

        full_table += "<details>\n"
        full_table += f"<summary>{icon} Configuration: `{config_name}`</summary>\n\n"
        full_table += "| Email | Date | Title | ? |\n"
        full_table += "|---|---|---|---|\n"

        for commit_hash, commit_email, commit_date, commit_title in reversed_commits:
            log_file = os.path.join(OUTPUT_DIR, config_name, f"{commit_hash}.log")
            status = _get_build_status_icon(log_file)
            
            commit_title_short = (commit_title[:51] + "...") if len(commit_title) > 54 else commit_title
            commit_email_user = commit_email.split('@')[0]
            log_path = os.path.join(OUTPUT_DIR, config_name, f"{commit_hash}.log")

            full_table += f"| {commit_email_user} | {commit_date} | [{commit_title_short}](./{log_path}) | {status} |\n"
        full_table += "\n</details>\n\n"

    with open(readme_path, "w") as f:
        f.writelines(header_lines)
        f.write(full_table)
