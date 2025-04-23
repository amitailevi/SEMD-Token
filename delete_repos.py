from github import Github
import os

def delete_all_repos():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise ValueError("Please set GITHUB_TOKEN environment variable")
    
    g = Github(token)
    user = g.get_user()
    
    repos_to_delete = [
        "smed",
        "SEMD-Trading-Bot",
        "smed_bot",
        "SEMD-unified",
        "SEMD-Platform"
    ]
    
    print("\n🗑️ מוחק את כל המאגרים הישנים...")
    for repo_name in repos_to_delete:
        try:
            repo = g.get_repo(f"amitailevi/{repo_name}")
            repo.delete()
            print(f"✅ המאגר {repo_name} נמחק בהצלחה")
        except Exception as e:
            print(f"❌ שגיאה במחיקת {repo_name}: {str(e)}")
    
    print("\n✨ מחיקת המאגרים הושלמה!")
    print("עכשיו נתחיל לבנות הכל מחדש בצורה מאורגנת")

if __name__ == "__main__":
    delete_all_repos() 