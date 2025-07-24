"""
AI‑powered code review bot for GitHub pull requests.

This script is intended to run as part of a GitHub Action.  When a pull
request is opened or updated, the action checks out the repository,
collects the diff, and sends it to an OpenAI model.  The model
generates a concise summary of the changes and suggests improvements
based on best practices.  The bot then posts its feedback as a comment
on the pull request.

To use this bot in your own repository, follow these steps:

1. Create a new GitHub repository and add the contents of the
   ``ai_code_review_bot`` folder.
2. Add an OpenAI API key and a GitHub token as secrets in your
   repository settings (``OPENAI_API_KEY`` and ``GITHUB_TOKEN``).
3. Push the repository to GitHub.  The included workflow will trigger
   whenever a pull request is opened or synchronized.

The script relies on the ``openai`` and ``PyGithub`` libraries.  The
model parameters (e.g. ``model`` and ``temperature``) can be tuned in
the code below.
"""

import json
import os
import subprocess
from pathlib import Path

import openai  # type: ignore
from github import Github  # type: ignore


def get_diff() -> str:
    """Return the git diff for the current pull request.

    The action checks out the PR before running this script, so
    ``git diff`` will produce the changes relative to the base branch.
    """
    result = subprocess.run(
        ["git", "--no-pager", "diff", "origin/main...HEAD"],
        stdout=subprocess.PIPE,
        text=True,
        check=True,
    )
    return result.stdout


def generate_review(diff: str, model: str = "gpt-3.5-turbo") -> str:
    """Use OpenAI API to generate a review summary and suggestions.

    Args:
        diff: The unified diff string.
        model: The OpenAI model to use.

    Returns:
        A string containing the AI‑generated review.
    """
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    if not openai.api_key:
        raise RuntimeError("OPENAI_API_KEY environment variable not set")
    prompt = (
        "You are a senior software engineer performing a code review.\n"
        "The following is a git diff for a pull request.\n\n"
        f"{diff}\n\n"
        "Please provide a concise summary of the changes and suggest any "
        "improvements or potential issues. Highlight best practices, security "
        "concerns, and potential performance optimizations."
    )
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.2,
    )
    return response.choices[0].message["content"].strip()


def post_comment(review_body: str) -> None:
    """Post the review comment on the pull request.

    Requires the following environment variables:
    - GITHUB_TOKEN: Personal access token or GitHub Actions token.
    - GITHUB_REPOSITORY: repo owner/name.
    - GITHUB_PR_NUMBER: pull request number.
    """
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("GITHUB_TOKEN environment variable not set")
    repo_name = os.environ.get("GITHUB_REPOSITORY")
    pr_number = os.environ.get("GITHUB_PR_NUMBER")
    if not (repo_name and pr_number):
        raise RuntimeError("GITHUB_REPOSITORY or GITHUB_PR_NUMBER not set")
    pr_number = int(pr_number)
    gh = Github(token)
    repo = gh.get_repo(repo_name)
    pr = repo.get_pull(pr_number)
    pr.create_issue_comment(review_body)


def main() -> None:
    diff = get_diff()
    if not diff.strip():
        print("No changes detected. Exiting without posting a comment.")
        return
    review = generate_review(diff)
    post_comment(review)
    print("Review posted successfully.")


if __name__ == "__main__":
    main()