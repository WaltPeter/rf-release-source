import subprocess

def check_git_status(repo_path):
    try:
        # Change to the specified repository directory
        subprocess.run(["cd", repo_path], check=True, shell=True)
        
        # Run 'git pull' and capture the output
        result = subprocess.run(
            ["git", "pull"],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Check the output to determine if it's up-to-date
        if "Already up to date." in result.stdout:
            print("The repository is already up-to-date.")
        else:
            print("The repository has been updated:")
            print(result.stdout)
            subprocess.run(["./convert.sh"], check=True, shell=True)
            subprocess.run(["./flash.sh"], check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e.stderr}")

check_git_status(".")