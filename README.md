# AI Code Review Bot 🤖

🚀 **Elevator pitch:** Bring a senior reviewer into every pull request. This GitHub Action uses ChatGPT to review your diffs, flagging bugs, style issues and security risks so you can merge confidently without burning time.

### Part of the Operator Meta Portfolio:
[Meta Portfolio](https://github.com/Bigmannot23/meta_portfolio) · [Operator Metrics Dashboard](https://github.com/Bigmannot23/operator_metrics_dashboard) · [AI Code Review Bot](#) · [Onboarding Assistant](https://github.com/Bigmannot23/Onboarding_Assistant) · [Job Offer Factory](https://github.com/Bigmannot23/job_offer_factory_autorun) · [Lexvion Compliance Engine](https://github.com/Bigmannot23/lexvion) · [Trading Bot](https://github.com/Bigmannot23/lexvion_trading_bot_full_auto) · [Leadscore API](https://github.com/Bigmannot23/operators-leadscore-api)

### Proof‑of‑ROI
- **3× faster reviews:** Developer feedback cycles shortened drastically【363497432291573†L4-L11】.
- **Defects prevented:** Over **30 issues** caught before they reached production【363497432291573†L4-L11】.
- **Style compliance:** 85% adherence to style guidelines after adoption【363497432291573†L4-L11】.

### What it does
- **Automated analysis:** Collects the diff of each pull request and sends it to ChatGPT for review【363497432291573†L45-L56】.
- **Customizable prompts:** Adjust the review style, model and temperature to match your team’s guidelines【363497432291573†L62-L73】.
- **Seamless integration:** Runs as a GitHub Action; comments appear directly on the PR【363497432291573†L21-L27】.
- **Extensible:** Modify the prompt or connect other models; add auto‑merge rules.

### Why it matters
Code reviews bottleneck releases. By automating the grunt work, you free senior developers to focus on architecture and mentorship while still enforcing quality. This tool shows that ChatGPT is ready for day‑to‑day code review tasks.

### Quickstart
1. Copy `.github/workflows/ai_code_review.yml` into your repo and adjust the `OPENAI_API_KEY` secret.
2. Tune the `model`, `temperature` and prompt variables in the workflow file【363497432291573†L62-L73】.
3. Open a pull request and watch the bot comment on your diff.
4. Address its feedback and merge; see the proof_of_roi.md for results.

### Operator principles
Follows automation first (AI reviews the code), modularity & reuse (plug‑n‑play GitHub Action), operator focus (developers save time and reduce errors) and compounding learning (the prompt can be improved by reading past bot comments).

### Related projects
- The **[Operator Metrics Dashboard](https://github.com/Bigmannot23/operator_metrics_dashboard)** instruments job search; apply similar instrumentation to measure code quality improvements.
- See **[Onboarding Assistant](https://github.com/Bigmannot23/Onboarding_Assistant)** for retrieval‑augmented Q&A capabilities.
- Explore the **[Meta Portfolio](https://github.com/Bigmannot23/meta_portfolio)** for case studies and ROI【918791940776565†L10-L24】.

---
