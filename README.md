# GitHub Repo Manager

Manage repositories in a GitHub account.

## GitHub Authentication

This project uses a Personal Access Token. Generate one in your GitHub account by going to Settings > Developer Settings > Personal access tokens, then generating a token with at least the full 'repo' scope.

## Usage

This project currently just creates or updates secrets using [PyGithub](https://github.com/PyGithub/PyGithub).

  1. Ensure you have Python and Pip installed.
  2. Install requirements: `pip3 install -r requirements.txt`
  3. Copy `example.config.yml` to `config.yml` and tweak it.
  4. Run the script: `python3 create_secret.py`.
  5. Enjoy!

> Note: Currently requires manual application of [this PR](https://github.com/PyGithub/PyGithub/pull/1681/files) to the PyGithub project. You can do this with:
>
> ```
> pip3 install git+https://github.com/PyGithub/PyGithub.git@refs/pull/1681/merge
> ```

## Author

[Jeff Geerling](https://www.jeffgeerling.com).
