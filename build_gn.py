import subprocess
import os

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
