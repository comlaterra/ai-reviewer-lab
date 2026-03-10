# ai-reviewer-lab

A workshop repository for building an AI code reviewer skill with Claude Code.

**You will not be running any code. The Python files are targets for your reviewer, not scripts to execute.**

---

## Setup (do this first, takes 2 minutes)

```bash
git clone https://github.com/[your-handle]/ai-reviewer-lab
cd ai-reviewer-lab
```

Then open the folder in Claude Code.

That is it. No installs. No environment variables. No configuration.

---

## What is in here

```
ai-reviewer-lab/
├── CLAUDE.md                          # The AI's context file. You will edit this.
├── src/
│   ├── api.py                         # A Flask API. Has problems planted in it.
│   ├── users.py                       # User service. Has problems planted in it.
│   └── payments.py                    # Payment service. Has problems planted in it.
└── .claude/
    └── skills/
        └── code-reviewer/
            └── SKILL.md               # The reviewer skill. You will complete this.
```

---

## Phase 1 (20 min): Scaffold

1. Open `CLAUDE.md` and read it top to bottom.
2. Look at the `⚠️ LAB TASK` comments. You will fill those in during the lab.
3. Open `.claude/skills/code-reviewer/SKILL.md` and read the skeleton.
4. Run the skill as-is to see what it catches with no customisation:

```
/code-reviewer src/api.py
```

Take note of what it finds and what it misses.

---

## Phase 2 (30 min): Write the Skill

1. Open `.claude/skills/code-reviewer/SKILL.md`.
2. Fill in the `Output Format` section. Decide what BLOCK, WARN, and PASS mean.
3. Fill in the `Constraints` section. What should this reviewer never do?
4. Add at least one real example from your actual codebase.
5. Run the skill again:

```
/code-reviewer src/payments.py
```

Did it catch more? Did anything change?

---

## Phase 3 (25 min): Tune

1. Open `CLAUDE.md` and fill in the `⚠️ LAB TASK` sections.
2. Add rules specific to your real codebase, not this fake one.
3. Run the reviewer on all three files:

```
/code-reviewer src/
```

4. Check the results. Is it signal or noise?
5. If it is flagging things that are not real problems, tighten the Constraints section.
6. If it is missing obvious things, add them to the `What the AI Should Flag Immediately` section in CLAUDE.md.

---

## Phase 4 (15 min): Commit and Plan

1. Save your SKILL.md and CLAUDE.md changes.
2. Decide: which real repo will you enable this on first?
3. Pick one metric to track for the first sprint. Override rate is a good start.
4. Group retro: what did the reviewer catch that surprised you? What did it miss?

---

## What is planted in the code

There are 12 problems across the three files. After the lab your facilitator will walk through all of them.

Try to find as many as possible with your reviewer before the debrief.
