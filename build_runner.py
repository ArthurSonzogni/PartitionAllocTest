import subprocess
import os
from settings import OUTPUT_DIR, REPO_DIR, GN_PATH

def _run_command(command, cwd, build_output):
    process = subprocess.run(command, cwd=cwd, capture_output=True, text=True)
    output = process.stdout + process.stderr
    print(output)
    process.check_returncode()
    return build_output + output

def _read_gn_args(config_path):
    args = []
    with open(config_path, 'r') as f:
        for line in f:
            line = line.strip().replace(" ", "")
            if line and not line.startswith('#'):
                args.append(line)
    return args

def check_commit_and_save_output(commit_hash, config_name, config_path):
    """
    Checks out a specific commit, runs the build process for a given configuration,
    and saves the output.
    Returns True if the build succeeds, False otherwise.
    """
    output_dir = os.path.join(OUTPUT_DIR, config_name)
    os.makedirs(output_dir, exist_ok=True)

    build_log_file = os.path.join(output_dir, f"{commit_hash}.log")

    if os.path.exists(build_log_file):
        print(f"Build log for commit {commit_hash} ({config_name}) already exists. Skipping...")
        return True

    build_output = ""
    try:
        print(f"Checking out commit: {commit_hash}")
        build_output = _run_command(["git", "checkout", commit_hash], REPO_DIR, build_output)

        print(f"Configuring build with {config_name}...")
        build_dir = os.path.join("out", config_name)
        gn_args = _read_gn_args(config_path)
        
        print(f"Using GN args: {' '.join(gn_args)}")
        configure_command = [GN_PATH, "gen", build_dir, f'--args={" ".join(gn_args)}']
        build_output = _run_command(configure_command, REPO_DIR, build_output)

        print(f"Running build with {config_name}...")
        build_command = ["ninja", "-C", build_dir]
        build_output = _run_command(build_command, REPO_DIR, build_output)

        print(f"Build completed for commit {commit_hash} ({config_name}).")
        return True

    except subprocess.CalledProcessError as e:
        print(f"Build failed for commit {commit_hash} ({config_name}).")
        build_output += e.stdout + e.stderr
        return False

    finally:
        with open(build_log_file, "w") as f:
            f.write(build_output)
