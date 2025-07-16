#!/usr/bin/env python3
import subprocess
import os
import glob

PARTITION_ALLOC_REPO = "https://chromium.googlesource.com/chromium/src/base/allocator/partition_allocator.git"
START_COMMIT = "087911ce77bce70f277fda09e10db56fe577ed53"
REPO_DIR = "partition_alloc"
OUTPUT_DIR = "output"
CONFIG_DIR = "configuration"
GN_PATH = os.path.join(os.getcwd(), "gn", "out", "gn")

# git clone https://gn.googlesource.com/gn
# cd gn
# python build/gen.py # --allow-warning if you want to build with warnings.
# ninja -C out
def build_gn():
    """
    Clones the GN repository and builds it.
    """
    gn_repo = "https://gn.googlesource.com/gn"
    gn_dir = "gn"

    if os.path.exists(gn_dir):
        # Fetch the latest changes if the directory already exists.
        subprocess.run(["git", "-C", gn_dir, "pull"], check=True)
        return
    
    subprocess.run(["git", "clone", gn_repo, gn_dir], check=True)
    subprocess.run(["python", "build/gen.py"], cwd=gn_dir, check=True)
    subprocess.run(["ninja", "-C", "out"], cwd=gn_dir, check=True)

def get_commits_after(start_commit):
    """
    Clones the PartitionAlloc repository and returns a list of commit hashes,
    their subjects, and author dates after the given start_commit, in chronological order.
    """
    if os.path.exists(REPO_DIR):
        # If the directory exists, fetch the latest changes.
        subprocess.run(["git", "-C", REPO_DIR, "fetch"], check=True)
        subprocess.run(["git", "-C", REPO_DIR, "checkout", "main"], check=True)
    else:
        subprocess.run(["git", "clone", PARTITION_ALLOC_REPO, REPO_DIR], check=True)
    
    output = subprocess.check_output([
        "git", "log", "--pretty=format:%H %ae %ad %s", "--date=short", f"{start_commit}..HEAD"
    ], cwd=REPO_DIR).decode("utf-8").strip()

    if not output:
        return []

    lines = output.split('\n')
    commits = []
    for line in lines:
        parts = line.split(' ', 3)
        if len(parts) == 4:
            commits.append((parts[0], parts[1], parts[2], parts[3]))
    
    commits.reverse()
    return commits

def get_configurations():
    """
    Returns a list of (configuration_name, configuration_path) tuples.
    """
    configs = []
    for config_path in glob.glob(os.path.join(CONFIG_DIR, "*.gn")):
        config_name = os.path.splitext(os.path.basename(config_path))[0]
        configs.append((config_name, config_path))
    return configs

def check_commit_and_save_output(commit_hash, config_name, config_path):
    """
    Checks out a specific commit, runs the build process for a given configuration,
    and saves the output.
    Returns True if the build succeeds, False otherwise.
    """
    output_dir = os.path.join(OUTPUT_DIR, config_name)
    os.makedirs(output_dir, exist_ok=True)

    output_prefix = os.path.join(output_dir, commit_hash)
    build_log_file = f"{output_prefix}.log"

    # Skip if the log file already exists.
    if os.path.exists(build_log_file):
        print(f"Build log for commit {commit_hash} ({config_name}) already exists. Skipping...")
        return True

    try:
        print(f"Checking out commit: {commit_hash}")
        subprocess.run(["git", "checkout", commit_hash], cwd=REPO_DIR, check=True,
                       capture_output=True)

        print(f"Configuring build with {config_name}...")
        build_dir = os.path.join("out", config_name)

        build_output = ""
        args=[]
        with open(config_path, 'r') as f:
            for line in f:
                line = line.strip()
                line = line.replace(" ", "")
                if line and not line.startswith('#'):
                    print(f"Adding GN arg: {line}")
                    args.append(line)

        print(f"Using GN args: {args}")
        configure_process = subprocess.run(
            [GN_PATH, "gen", build_dir, f'--args={' '.join(args)}'],
            cwd=REPO_DIR,
            capture_output=True, text=True
        )
        build_output = configure_process.stdout + configure_process.stderr
        print(build_output)
        configure_process.check_returncode()

        build_output = configure_process.stdout + configure_process.stderr
        print(build_output)
        configure_process.check_returncode()

        print(f"Running build with {config_name}...")
        build_process = subprocess.run(["ninja", "-C", build_dir], cwd=REPO_DIR,
                                       capture_output=True, text=True)
        build_output += build_process.stdout + build_process.stderr
        build_process.check_returncode()

        with open(build_log_file, "w") as f:
            f.write(build_output)

        print(f"Build completed for commit {commit_hash} ({config_name}).")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Build failed for commit {commit_hash} ({config_name}).")
        
        with open(build_log_file, "w") as f:
            f.write(build_output)

        return False
    finally:
        pass

def update_readme(commits, configurations):
    """
    Updates README.md with tables of build results for each configuration.
    """
    readme_path = "README.md"
    
    with open(readme_path, "r") as f:
        lines = f.readlines()
    
    header_lines = []
    for line in lines:
        if line.strip() == "## Build Results":
            break
        header_lines.append(line)

    full_table = "## Build Results\n\n"

    reversed_commits = list(reversed(commits))

    for config_name, _ in configurations:
        # Determine icon from the latest commit
        icon = "⚪" 
        if reversed_commits:
            latest_commit_hash = reversed_commits[0][0]
            log_file = os.path.join(OUTPUT_DIR, config_name, f"{latest_commit_hash}.log")
            with open(log_file, "r") as f:
                content = f.read()
                if "ERROR" in content:
                    icon = "❌"
                elif "FAILED" in content:
                    icon = "❌"
                else:
                    icon = "✅"

        full_table += "<details>\n"
        full_table += f"<summary>{icon} Configuration: `{config_name}`</summary>\n\n"
        full_table += "| Email | Date | Title | ? |\n"
        full_table += "|---|---|---|---|\n"


        for commit_hash, commit_email, commit_date, commit_title, in reversed_commits:
            log_file = os.path.join(OUTPUT_DIR, config_name, f"{commit_hash}.log")
            status = "❌"
            with open(log_file, "r") as f:
                content = f.read()
                if "ERROR" in content:
                    status = "❌"
                elif "FAILED" in content:
                    status = "❌"
                else:
                    status = "✅"
            
            if len(commit_title) > 54:
                commit_title = commit_title[:51] + "..."

            commit_email = commit_email.split('@')[0]
            log_path = os.path.join(OUTPUT_DIR, config_name, f"{commit_hash}.log")
            full_table += f"| {commit_email} | {commit_date} | [{commit_title}](./{log_path}) | {status} |\n"
        full_table += "\n</details>\n\n"

    with open(readme_path, "w") as f:
        f.writelines(header_lines)
        f.write(full_table)

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
