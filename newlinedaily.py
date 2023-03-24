import os
from github import Github

# Authenticate to GitHub using a personal access token
g = Github(os.environ['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'])

# Replace OWNER and REPO_NAME with your GitHub username and repository name, respectively
repo = g.get_repo('KLuering/AutoUpdateApp')

# Replace COMMIT_MESSAGE and CODE_LINE with your desired commit message and code line, respectively
commit_message = 'Add daily code line'
code_line = 'print("Hello, world!")\n'

# Create a new file with today's date as the file name
today = datetime.date.today().strftime('%Y-%m-%d')
filename = f'{today}.py'

# Create the file in the repository
repo.create_file(filename, commit_message, code_line)

# Commit and push the changes to the repository
branch = repo.get_branch('main')
branch.edit_protection(False)
commit = branch.commit.commit
tree = repo.get_git_tree(commit.sha, recursive=True)
element = tree.tree[0]
new_tree = repo.create_git_tree([element], tree.base_tree)
new_commit = repo.create_git_commit(commit_message, new_tree, [commit])
branch.edit_protection(True)
branch.update_commit(new_commit.sha)
