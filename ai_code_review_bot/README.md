# AI Code Review Bot


## 📈 Proof‑of‑ROI Quick Stats

Deploying an automated code review assistant not only improves code quality—it saves your team time and mental energy.  Here are example metrics you can track once the bot is in use:

- **Average review time saved:** `{{ insert hours per PR here }}` – by automatically summarizing diffs and suggesting improvements, reviewers can focus on high‑impact feedback.
- **Defects prevented:** `{{ insert number of bugs caught }}` – issues flagged early by the bot reduce downstream bug fixes and hotfixes.
- **Style guideline adherence:** `{{ insert compliance increase }}` – a configurable prompt ensures your codebase stays consistent with team standards.

These statistics can be logged via your CI pipeline or simple scripts.  Summarize them in your portfolio to demonstrate the tangible benefits of AI‑assisted code reviews.

Elevate your pull‑request workflow with an AI‑powered code reviewer.  This
repository contains a Python script and GitHub Action that automatically
analyzes code changes using OpenAI’s ChatGPT models and posts a review
comment summarizing the changes and suggesting improvements.

## ✨ Features

- **Automated insights:** Generates a concise summary of the pull request
  diff and highlights potential improvements, best practices, and
  performance or security issues.
- **Seamless integration:** Runs as a GitHub Action on each pull request.
- **Customizable:** Tune the model, temperature, and prompts to suit your
  codebase and team standards.

## 🚀 Setup

1. Create a new repository or add this folder to your existing repo.
2. Add the following secrets to your GitHub repository settings:
   - `OPENAI_API_KEY`: Your OpenAI API key.  Sign up at
     [platform.openai.com](https://platform.openai.com/) if you don’t
     already have one.
   - `GITHUB_TOKEN`: A personal access token with permission to comment on
     pull requests.  Alternatively, use the default `${{ github.token }}`
     provided by Actions.
3. Commit and push the code.  The workflow defined in
   `.github/workflows/code_review.yml` will trigger on pull request events.

4. Review and adjust the configuration in `config.json`.  You can choose which model to use (e.g. `gpt-3.5-turbo` vs. `gpt-4`), the temperature of AI responses, and customize the system prompt.  See the *Configuration* section below for details.

## 🧠 How It Works

The action runs `ai_code_review_bot/review.py`, which performs the
following steps:

1. Runs `git diff origin/main...HEAD` to gather the changes introduced
   by the pull request.
2. Sends the diff to the OpenAI Chat API with a prompt instructing the
   model to summarize the changes and suggest improvements.
3. Posts the generated feedback as a comment on the pull request via the
   GitHub API.

You can modify the prompt or change the model (e.g. to `gpt-4`) in
`review.py` to tailor the reviews to your needs.

## 🔐 Security & Privacy

The code review bot uses OpenAI’s API.  **Never** hardcode your API key in the repository.  Instead, define the `OPENAI_API_KEY` secret in your GitHub repository settings.  Similarly, use the provided `${{ github.token }}` for posting comments—no need to store personal tokens unless you require additional permissions.  The bot only processes the diff of a pull request and does not persist source code outside of the review context.

## 🛠️ Configuration

Behavior of the bot is driven by `config.json`.  A sample configuration is included:

```json
{
  "model": "gpt-3.5-turbo",
  "temperature": 0.2,
  "max_tokens": 500,
  "system_prompt": "You are an expert code reviewer. Summarize the changes and suggest improvements, best practices, performance and security fixes.",
  "context_lines": 5
}
```

| Key | Description |
| --- | --- |
| `model` | Which OpenAI Chat completion model to use. |
| `temperature` | Controls the randomness of the generated output. |
| `max_tokens` | Maximum number of tokens for the response. |
| `system_prompt` | Defines the persona and tasks for the assistant. |
| `context_lines` | How many lines of context around each change to include in the prompt. |

You can modify this file to tune the bot to your codebase or organization.  For example, increase `context_lines` for larger diffs or adjust the prompt to enforce specific style guides.

## 🧪 Unit Tests & Continuous Integration

A `tests/` directory is provided containing basic tests that ensure the configuration can be loaded and that the review script exists.  Run them with `python -m unittest discover tests`.  The supplied GitHub Action executes these tests on each pull request and displays the result via the badge at the top of this README.

## 📄 Files

- `review.py`: Main script that performs the review and posts a comment.
- `.github/workflows/code_review.yml`: GitHub Action workflow file.
- `requirements.txt`: Python dependencies.

## 💡 Demonstrating Impact

Including this project in your portfolio shows that you can extend AI
capabilities into software engineering workflows.  It highlights
familiarity with GitHub APIs, CI/CD, and prompt engineering—skills
that recruiters and engineering leaders find valuable.
