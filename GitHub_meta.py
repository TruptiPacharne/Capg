import requests
import json

# Replace these with your actual GitHub username and repository name
owner = "TruptiPacharne"
repo = "capg"

# GitHub API URL
url = f"https://api.github.com/repos/{owner}/{repo}"

# Send a GET request to the GitHub API
response = requests.get(url)

if response.status_code == 200:
    repo_data = response.json()

    # Create a Model Context Protocol-like structure
    model_context = {
        "repository": {
            "name": repo_data.get("name"),
            "full_name": repo_data.get("full_name"),
            "description": repo_data.get("description"),
            "owner": repo_data.get("owner", {}).get("login"),
            "url": repo_data.get("html_url"),
            "created_at": repo_data.get("created_at"),
            "updated_at": repo_data.get("updated_at"),
            "pushed_at": repo_data.get("pushed_at"),
            "language": repo_data.get("language"),
            "stargazers_count": repo_data.get("stargazers_count"),
            "watchers_count": repo_data.get("watchers_count"),
            "forks_count": repo_data.get("forks_count"),
            "open_issues_count": repo_data.get("open_issues_count"),
            "default_branch": repo_data.get("default_branch")
        }
    }

    # Save to JSON file
    with open("repository_metadata.json", "w") as json_file:
        json.dump(model_context, json_file, indent=4)

    print("🔑 Key created: repository_metadata.json")
else:
    print(f"❌ Failed to fetch metadata. Status code: {response.status_code}")
