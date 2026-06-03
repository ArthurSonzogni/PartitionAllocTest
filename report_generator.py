import os
from settings import OUTPUT_DIR

def get_build_status_icon(log_file_path):
    """
    Determines the build status icon based on the content of the log file.
    """
    if not os.path.exists(log_file_path):
        return "⬜"
        
    with open(log_file_path, "r") as f:
        content = f.read()
        if "ERROR" in content or "FAILED" in content:
            return "🟥"
        return "🟩"

def update_readme(commits, configurations):
    """
    Updates README.md with a single table of build results.
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

    full_content = "## Build Results\n\n"
    reversed_commits = list(reversed(commits))

    # Sort configurations by name to ensure consistent column order
    sorted_configurations = sorted(configurations, key=lambda x: x[0])

    # Generate table header
    config_names = [config_name for config_name, _ in sorted_configurations]
    header = "| Email | Date | Title | " + " | ".join([name.capitalize() for name in config_names]) + " |\n"
    separator = "|---|---|---|" + "---|" * len(config_names) + "\n"
    
    full_content += header
    full_content += separator

    for commit_hash, commit_email, commit_date, commit_title in reversed_commits:
        commit_title_short = (commit_title[:51] + "...") if len(commit_title) > 54 else commit_title
        commit_email_user = commit_email.split('@')[0]
        
        row = f"| {commit_email_user} | {commit_date} | {commit_title_short} |"
        
        for config_name, _ in sorted_configurations:
            log_file = os.path.join(OUTPUT_DIR, config_name, f"{commit_hash}.log")
            status = get_build_status_icon(log_file)
            log_path = os.path.join(OUTPUT_DIR, config_name, f"{commit_hash}.log")
            
            if status != "⬜":
                row += f" [{status}](./{log_path}) |"
            else:
                row += f" {status} |"
        
        full_content += row + "\n"

    with open(readme_path, "w") as f:
        f.writelines(header_lines)
        f.write(full_content)
