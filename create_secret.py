# GitHub Secret Manager
#
# Yeah, it's pretty raw. But I needed to do it quick.
#
# Set GITHUB_USERNAME to your username.
# Set GITHUB_PASSWORD to your password.

from github import Github
import os
import yaml

# Get config.
with open("config.yml", 'r') as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

# Authenticate.
g = Github(config["personal_access_token"])

# Loop through repositories.
for repo in g.get_user().get_repos():
    # Get filtered list of repositories that are not archived.
    if (not repo.archived and config["repo_name_filter"] in repo.full_name):
        print(repo.full_name)
