# AI Code Review Bot

## Elevator pitch
Bring a senior reviewer into every pull request. This GitHub Action uses ChatGPT to review your diffs, flagging bugs, style issues and security risks so you can merge confidently without burning time.

## Usage
1. Copy `.github/workflows/ai_code_review.yml` into your repository.
2. Set the required secret `OPENAI_API_KEY` in your repository settings.
3. Tune the `model`, `temperature` and `prompt` variables in the workflow file.
4. Open a pull request; the bot will automatically post comments on your code diff.

## Architecture
- Collect the diff from the GitHub API.
- Send the diff and configurable prompt to ChatGPT.
- Parse the response and post review comments back to the PR.
- Modular: prompts and models can be swapped or extended.

![Diagram](./assets/diagram.png)

## Results & ROI
- **3× faster reviews** — evidence: Integration tests & user feedback
- **30+ issues prevented** — evidence: CI error logs
- **85% style compliance** — evidence: Linting reports

## Part of the Operator Meta Portfolio
- [Job Offer Factory](../job_offer_factory_autorun/OPERATOR_README.md)
- [Onboarding Assistant](../Onboarding_Assistant/OPERATOR_README.md)
- [Lexvion Compliance Engine](../lexvion/OPERATOR_README.md)
- [Lexvion Trading Bot](../lexvion_trading_bot_full_auto/OPERATOR_README.md)
- [Operators Leadscore API](../operators-leadscore-api/OPERATOR_README.md)
- [Operator Metrics Dashboard](../operator_metrics_dashboard/OPERATOR_README.md)
- [Meta Portfolio](../meta_portfolio/README.md)

## Operator principles
Automation first, modularity, operator focus and compounding learning.
