# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agentic Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I used Claude Code (the desktop app's Code tab) as an agent to build the core project end to end: clone my fork, set up the virtual environment, expand the dataset, implement the recommender, run and evaluate it, write the README and model card, and commit and push the work.

**Prompts used:**

1. I pasted the full assignment instructions (Phases 1–5) as the prompt, with no extra wording, so the agent had to plan the steps itself.
2. After reviewing its summary, I replied: "Push it."

**What did the agent generate or change?**

- **Setup:** found my GitHub username from the remotes of my other AI110 repos, confirmed my fork existed, cloned it into `Downloads/AI110`, created `.venv`, installed `requirements.txt`, and ran `pytest` on the starter (2 passed).
- **`data/songs.csv`:** added 10 songs (ids 11–20) in new genres and moods: hip-hop, classical, metal, country, R&B, EDM, reggae, folk, blues, K-pop.
- **`src/recommender.py`:** implemented `load_songs` (csv.DictReader plus numeric conversion), `score_song` (genre +2.0, mood +1.0, energy closeness up to +1.5, acoustic fit up to +0.5, returning a score and a list of reasons), and `recommend_songs` (scores every song, `sorted()` highest first, top k). Also filled in the `Recommender` class so the tests use the same scoring, and added `DEFAULT_WEIGHTS` / `EXPERIMENT_WEIGHTS`.
- **`src/main.py`:** five profiles (three normal, two adversarial), a readable output format with the reasons, and an `--experiment` flag for the weight shift (energy ×2, genre ×½).
- **`README.md` and `model_card.md`:** filled every section, including the pasted terminal output for each profile, pairwise profile comparisons, the experiment results table, and the bias write-up.
- **Git:** three commits (dataset, implementation, docs), then `git push origin main` after I approved.

**What did you verify or fix manually?**

- **Starter bug:** the starter `main.py` used `from recommender import ...`, which crashes when run as `python -m src.main`. It was changed to `from src.recommender import ...`.
- **Pasted output matches a real run:** the agent diffed the code blocks in `model_card.md` against a fresh run of `python -m src.main`; they matched exactly. It also corrected a wrong count in the README (it first said 16 genres; the catalog has 17, and 15 of them have only one song).
- **Push only after review:** the agent committed locally and asked before pushing to my public repo. I read the summary first, then told it to push.
- **Still on me:** the personal reflection in `model_card.md` and `README.md` started as an AI draft, so I need to rewrite it in my own words. I also need to spot-check the scoring math for one song myself (e.g., Sunrise City for the pop profile: 2.00 + 1.00 + 1.5 × (1 − 0.02) + 0.5 × (1 − 0.18) = 4.88).

---

## Design Pattern (SF10)

> Document how AI helped you choose or implement a design pattern.

**Which design pattern did you use?**

<!-- Not attempted -->

**How did AI help you brainstorm or implement it?**

<!-- Not attempted -->

**How does the pattern appear in your final code?**

<!-- Not attempted -->
