import requests
import os
import subprocess
from requests.auth import HTTPBasicAuth
import webbrowser

def clone_github_repo(repo_url, workspace_path):
    # Extract repository owner and name from URL
    _, _, _, owner, repo_name = repo_url.split('/')

    # Create directory for workspace if it doesn't exist
    if not os.path.exists(workspace_path):
        os.makedirs(workspace_path)

    # Clone the repository
    clone_url = f"https://github.com/akumarseth/pk.git"
    os.system(f"git clone {clone_url} {workspace_path}")

    print(f"Repository '{repo_name}' cloned successfully to '{workspace_path}'")
    

def open_folder_in_code_server(folder_path):
    code_server_url = "http://localhost:8080"
    api_endpoint = "/api/open"
    full_url = code_server_url + api_endpoint

    payload = {
        "path": folder_path
    }
    
    username = "user"  # Default username for Code Server
    password = "Admin@123"  # Your password for Code Server

    try:
        response = requests.post(full_url, json=payload, auth=HTTPBasicAuth(username, password))
        if response.status_code == 200:
            print("Folder opened successfully.")
            webbrowser.open_new_tab(code_server_url + "/workspace/" + folder_path)
        else:
            print("Failed to open folder. Status code:", response.status_code)
            print("Error message:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error making request:", e)




if __name__ == "__main__":
    # GitHub repository URL
    repo_url = "https://github.com/username/repo_name"

    # Path to Code Server workspace
    folder_path_to_open = "clone_path/akumarseth"
    
    # Example usage:
    open_folder_in_code_server(folder_path_to_open)
