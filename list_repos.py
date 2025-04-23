from github import Github
import os

def list_repos():
    token = os.getenv("GITHUB_TOKEN")  # Get token from environment variable
    if not token:
        raise ValueError("Please set GITHUB_TOKEN environment variable")
    g = Github(token)
    user = g.get_user()
    
    print("\n📚 Your GitHub Repositories:")
    print("=" * 50)
    
    for repo in user.get_repos():
        print(f"• {repo.name}")
        print(f"  URL: {repo.html_url}")
        print(f"  Description: {repo.description}")
        print(f"  Archived: {repo.archived}")
        print("-" * 30)

if __name__ == "__main__":
    list_repos() 