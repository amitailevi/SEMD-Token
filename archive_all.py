from github import Github
import os

def archive_all_repos():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("❌ אנא הגדר את הטוקן הקיים שלך כמשתנה סביבה")
        return
        
    g = Github(token)
    user = g.get_user()
    
    repos_to_archive = [
        "smed",
        "SEMD-Trading-Bot",
        "smed_bot",
        "SEMD-unified",
        "SEMD-Platform"
    ]
    
    print("\n🔒 מארכב את כל המאגרים הישנים...")
    for repo_name in repos_to_archive:
        try:
            repo = g.get_repo(f"amitailevi/{repo_name}")
            repo.edit(archived=True)
            print(f"✅ המאגר {repo_name} אורכב בהצלחה")
        except Exception as e:
            print(f"❌ שגיאה בארכוב {repo_name}: {str(e)}")
    
    print("\n✨ התהליך הושלם!")
    print("עכשיו המאגרים מאורכבים ולא יופיעו בדף הראשי")
    print("אתה יכול להתחיל נקי עם מאגר חדש כשתרצה")

if __name__ == "__main__":
    archive_all_repos() 