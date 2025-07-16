import subprocess
import os
from settings import REPO_DIR, PARTITION_ALLOC_REPO

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

