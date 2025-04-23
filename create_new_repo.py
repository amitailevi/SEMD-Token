from github import Github
import os

def create_new_repo():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise ValueError("Please set GITHUB_TOKEN environment variable")
    
    g = Github(token)
    user = g.get_user()
    
    print("\n🚀 יוצר מאגר חדש ומאוחד...")
    
    try:
        repo = user.create_repo(
            name="SEMD-Token",
            description="SEMD Token - Advanced DeFi Platform on Solana | Trading Bot | Smart Contracts | Analytics",
            homepage="",
            private=False,
            has_issues=True,
            has_wiki=True,
            has_downloads=True,
            has_projects=True
        )
        print("✅ המאגר החדש נוצר בהצלחה!")
        return repo
    except Exception as e:
        print(f"❌ שגיאה ביצירת המאגר: {str(e)}")
        return None

if __name__ == "__main__":
    create_new_repo() 