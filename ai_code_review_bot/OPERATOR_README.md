# Operator Guide – AI Code Review Bot

This guide is for operators who want to enable automated pull‑request reviews using the **AI Code Review Bot**.  It explains setup, configuration, running and testing the bot, and how to extend or troubleshoot it.

## 🧰 Setup

1. **Add the bot to your repository.**  Copy the `ai_code_review_bot/` folder into the root of the target repository.
2. **Create GitHub secrets.**
   - `OPENAI_API_KEY` – your OpenAI API key used to call the Chat completion endpoint.  Obtain one from [platform.openai.com](https://platform.openai.com/).
   - `GITHUB_TOKEN` – a personal access token with permission to post comments on pull requests.  You can rely on `${{ github.token }}` provided by GitHub Actions for most cases.
3. **Review the configuration.**  Open `config.json` and set the model, temperature, max tokens, and system prompt to your preferences.  Do not include your API key here.
4. **Commit and push.**  The workflow in `.github/workflows/code_review.yml` will run on each pull request, invoke the bot, and post a comment with the summary and suggestions.

## ⚙️ Configuration Options

All user‑tunable parameters live in `config.json`:

| Field | Purpose |
| --- | --- |
| `model` | Which OpenAI Chat model to call.  Use `gpt-3.5-turbo` for cost‑effectiveness or upgrade to `gpt-4` for deeper analysis. |
| `temperature` | Controls randomness.  Lower numbers yield more deterministic responses. |
| `max_tokens` | Upper bound on the length of the AI’s reply. |
| `system_prompt` | The initial system message that sets expectations for the model.  Customize it to match your team’s guidelines. |
| `context_lines` | Number of unchanged lines around each diff hunk to include in the prompt. |

Changes to `config.json` take effect the next time the workflow runs—no code changes needed.

## ▶️ How to Run & Test

To manually invoke the bot locally:

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...  # set your API key
python review.py
```

This will collect the diff between your local `HEAD` and `origin/main`, call the OpenAI API, and print the feedback.  When running via GitHub Actions, the bot automatically picks up the diff of the pull request.

Run the unit tests with:

```bash
python -m unittest discover tests
```

These tests ensure that `config.json` is valid JSON and that the review script exists.

## 🔧 How to Extend or Fork

- **Different code hosts:** Adapt the GitHub Action to run in GitLab, Bitbucket, or Azure DevOps by changing the workflow syntax.  The Python script itself is agnostic to the CI environment.
- **Custom prompts:** Edit `system_prompt` in `config.json` to enforce coding standards, request additional analysis (e.g. security reviews), or adjust the tone of the feedback.
- **Logging and analytics:** Modify `review.py` to log usage statistics (e.g. response time, token counts) and feed them into a dashboard.
- **Language support:** The current implementation assumes diff output is English.  You can augment the prompt to support other languages or integrate translation APIs.

## 🛠️ Troubleshooting Tips

| Problem | Solution |
| --- | --- |
| **No comment posted on pull request** | Ensure the workflow file exists at `.github/workflows/code_review.yml` and that it runs on `pull_request` events.  Check the Actions tab for errors. |
| **Invalid API key errors** | Confirm that your `OPENAI_API_KEY` secret is defined in the repository settings and has not expired. |
| **Large diffs cause timeouts or high costs** | Reduce `max_tokens` or `context_lines`, or modify the script to limit the amount of code sent to the API (e.g. only changed lines). |
| **Unwanted suggestions** | Tailor `system_prompt` to focus on the aspects of your codebase that matter most (performance, readability, security, etc.). |

This operator guide should enable you to confidently deploy, customize, and maintain the **AI Code Review Bot** as part of your CI/CD pipeline.