import urllib.request
import json
import os

def main():
    repo = "ArthurSonzogni/PartitionAlloc"
    url = f"https://api.github.com/repos/{repo}/commits?per_page=100"
    
    mapping = {}
    mapping_file = "author_map.json"
    
    if os.path.exists(mapping_file):
        try:
            with open(mapping_file, "r") as f:
                mapping = json.load(f)
        except Exception as e:
            print(f"Warning: could not load existing mapping: {e}")

    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        token = os.environ.get("GITHUB_TOKEN")
        if token:
            headers['Authorization'] = f"token {token}"
            
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            commits = json.loads(response.read().decode())
            
        new_entries = 0
        for commit in commits:
            author = commit.get('author')
            if author:
                github_user = author.get('login')
                commit_author = commit.get('commit', {}).get('author', {})
                email = commit_author.get('email')
                
                if github_user and email:
                    email_prefix = email.split('@')[0]
                    if "noreply" not in email:
                        if email_prefix not in mapping or mapping[email_prefix] != github_user:
                            mapping[email_prefix] = github_user
                            new_entries += 1
                        
        mapping['arthursonzogni'] = 'ArthurSonzogni'
        
        with open(mapping_file, "w") as f:
            json.dump(mapping, f, indent=2)
            
        print(f"Updated author_map.json. Total entries: {len(mapping)} (Added {new_entries} new)")
        
    except Exception as e:
        print(f"Warning: Failed to update author map from GitHub API: {e}")
        print("Continuing with existing map.")

if __name__ == "__main__":
    main()
