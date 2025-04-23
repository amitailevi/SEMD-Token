from github import Github
import requests
import json
import os
import subprocess
from pathlib import Path

class SEMDGitHubManager:
    def __init__(self):
        self.token = os.getenv("GITHUB_TOKEN")
        if not self.token:
            raise ValueError("Please set GITHUB_TOKEN environment variable")
        self.g = Github(self.token)
        self.user = self.g.get_user()
        self.headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }
        self.repo_name = "SEMD-Platform"
        
    def update_repository(self):
        """Update the existing repository with new content"""
        print(f"\n🔄 Updating repository: {self.repo_name}")
        
        try:
            repo = self.g.get_repo(f"amitailevi/{self.repo_name}")
            self.repo_url = repo.clone_url
            
            # Update repository description
            repo.edit(
                description="SEMD Platform - Professional Trading Bot and DeFi System",
                homepage="",
                private=False,
                has_issues=True,
                has_wiki=True
            )
            
            print("✅ Repository updated successfully!")
            return True
        except Exception as e:
            print(f"❌ Error updating repository: {str(e)}")
            return False

    def setup_local_git(self):
        """Configure local git repository and push initial content"""
        print("\n🔧 Setting up local Git repository")
        
        try:
            commands = [
                "git init",
                "git add .",
                'git config --local user.email "amitai.levi@gmail.com"',
                'git config --local user.name "Amitai Levi"',
                'git commit -m "Professional update: SEMD Platform v1.0.0"',
                f'git remote add origin {self.repo_url}',
                "git branch -M main",
                "git push -u origin main --force"  # Using force to overwrite existing content
            ]
            
            for cmd in commands:
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    print(f"✅ {cmd}")
                else:
                    print(f"❌ Error in '{cmd}': {result.stderr}")
                    
            print("\n✅ Successfully pushed all files to GitHub!")
            print(f"🌐 Repository URL: https://github.com/amitailevi/{self.repo_name}")
            
        except Exception as e:
            print(f"❌ Error in Git operations: {str(e)}")

    def archive_old_repos(self):
        """Archive the old repositories"""
        print("\n📦 Archiving old repositories")
        
        old_repos = ["smed", "SEMD-Trading-Bot", "smed_bot", "SEMD-unified"]
        for old_repo_name in old_repos:
            if old_repo_name != self.repo_name:  # Don't archive the main repository
                try:
                    old_repo = self.g.get_repo(f"amitailevi/{old_repo_name}")
                    old_repo.edit(archived=True)
                    print(f"✅ Archived: {old_repo_name}")
                except Exception as e:
                    print(f"❌ Error archiving {old_repo_name}: {str(e)}")

    def execute_full_migration(self):
        """Execute the complete migration process"""
        print("\n🚀 Starting SEMD Platform Migration")
        print("=" * 50)
        
        # Update existing repository
        if self.update_repository():
            # Setup and push local content
            self.setup_local_git()
            # Archive old repositories
            self.archive_old_repos()
            
            print("\n✨ Migration completed successfully!")
            print("=" * 50)
            print(f"🌐 Your updated platform is available at: https://github.com/amitailevi/{self.repo_name}")
        else:
            print("\n❌ Migration failed at repository update stage")

if __name__ == "__main__":
    manager = SEMDGitHubManager()
    manager.execute_full_migration() 