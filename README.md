# ai-reviewer-lab

A workshop for building an AI code reviewer skill with Claude Code.

**You will not be running any code. The Python files are review targets, not scripts to execute.**

---

## Setup

```bash
git clone https://github.com/[your-handle]/ai-reviewer-lab
cd ai-reviewer-lab
```

Open the folder in Claude Code. That is it — no installs, no configuration.

### Using GitHub Copilot (VS Code agent mode)

This lab also works with GitHub Copilot in VS Code agent mode. Enable these two settings:

1. **Chat: Use Claude Md File** — turn this **on** so Copilot reads `CLAUDE.md` instructions from your workspace.
2. **Chat: Agent Skills Locations** — add `.claude/skills` so Copilot can discover the skills in this repo.

---

## Project structure

```
ai-reviewer-lab/
├── CLAUDE.md                     # AI context file — you will edit this
├── requirements.txt
├── Makefile
├── src/
│   ├── app.py                    # Flask app factory
│   ├── config.py                 # Configuration loader
│   ├── auth.py                   # Auth decorators
│   ├── models.py                 # Database helpers
│   ├── utils.py                  # Validators and helpers
│   ├── api/
│   │   ├── users.py              # User endpoints
│   │   └── payments.py           # Payment endpoints
│   └── services/
│       ├── users.py              # User business logic
│       └── payments.py           # Payment business logic
├── tests/
│   └── test_users.py             # API tests
└── .claude/
    └── skills/
        └── code-reviewer.md      # The skill you will build
```

---

## Phase 1 — Scaffold (20 min)

1. Read `CLAUDE.md` top to bottom.
2. Note the LAB TASK sections — you will fill these in.
3. Open `.claude/skills/code-reviewer.md` and read the skeleton.
4. Run the skill as-is to see what it catches with no customisation:

```
/code-reviewer src/
```

Take note of what it finds and what it misses.

---

## Phase 2 — Write the Skill (30 min)

1. Open `.claude/skills/code-reviewer.md`.
2. Define your output format — what do BLOCK, WARN, and PASS mean?
3. Write the Constraints section — what should this reviewer never do?
4. Add at least one real-world example.
5. Run the skill again on a specific file:

```
/code-reviewer src/services/payments.py
```

Did it catch more? Did anything change?

---

## Phase 3 — Tune (25 min)

1. Fill in the LAB TASK sections in `CLAUDE.md`.
2. Add rules specific to your real codebase, not this one.
3. Run the reviewer on the full source tree:

```
/code-reviewer src/
```

4. Is it signal or noise? Tighten Constraints if it over-flags. Add rules if it under-flags.

---

## Phase 4 — Commit and Plan (15 min)

1. Save your changes to SKILL.md and CLAUDE.md.
2. Decide which real repo you will enable this on first.
3. Pick one metric to track. Override rate is a good start.
4. Group retro: what did your reviewer catch that surprised you? What did it miss?

---

## What is planted

There are 12 problems across the source files. Your facilitator will walk through all of them after the lab.

Try to catch as many as possible with your reviewer before the debrief.
