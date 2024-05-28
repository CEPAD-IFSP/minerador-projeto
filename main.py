import os
import requests
from dotenv import load_dotenv

load_dotenv()

OUTPUT_FILE = 'data/github_issues.txt'
TOKEN = os.getenv('GITHUB_TOKEN')  
REPO_OWNER = os.getenv('REPO_OWNER') 
REPOS = [repo.strip() for repo in os.getenv('REPOS').split(',')]

def get_issues(owner: str, 
               repo: str, 
               token: str) -> dict:
    issues_url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    headers = {'Authorization': f'token {token}'}
    params = {'state': 'all'}
    response = requests.get(issues_url, 
                            headers=headers, 
                            params=params)
    response.raise_for_status()
    return response.json()

def save_issues_to_txt_file(issues: str, 
                        filename: str, 
                        repo_name: str):
    with open(filename, 'a') as file:
        file.write(f"--- Issues for {repo_name} ---\n")
        for issue in issues:
            file.write(f"Issue #{issue['number']} - {issue['title']}\n")
            file.write(f"URL: {issue['html_url']}\n")
            file.write(f"State: {issue['state']}\n")
            file.write(f"Body: {issue['body']}\n\n")

def main():
    open(OUTPUT_FILE, 'w').close()
    for repo in REPOS:
        print(f"Fetching issues for {repo}...")
        issues = get_issues(REPO_OWNER, repo, TOKEN)
        save_issues_to_txt_file(issues, OUTPUT_FILE, repo)
    print(f"Data has been written to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()