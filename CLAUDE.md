# CLAUDE.md

This file defines how AI tools should behave in this codebase.
Read this before writing, reviewing, or modifying any code.

---

## Architecture

This is a REST API built with Flask and SQLite.
Business logic lives in service modules (`users.py`, `payments.py`).
The API layer (`api.py`) handles routing and request validation only.

> ⚠️ LAB TASK: Is this actually true of the code you see? What is missing from this description?

---

## Hard Rules

- Never put secrets or credentials in source code. Use environment variables.
- Every endpoint must validate input before passing it to a service function.
- Errors returned to the client must never include internal stack traces or raw exception messages.

> ⚠️ LAB TASK: Add 2 or 3 rules specific to YOUR real codebase here.
> Think about the mistakes your team makes repeatedly.

---

## Auth

> ⚠️ LAB TASK: This section is intentionally empty.
> Describe how authentication works in this system. Who is allowed to call what?
> What should the AI assume if an endpoint has no auth check?

---

## Never Do This

- Raw SQL string formatting (use parameterised queries always)
- Catching exceptions and swallowing them silently

> ⚠️ LAB TASK: What else belongs here for your stack?

---

## Payments

Any code that touches `payments.py` is high risk.
Treat it with extra scrutiny. Flag anything that moves money without an audit trail.

---

## What the AI Should Flag Immediately

- Hardcoded strings that look like API keys, tokens, or passwords
- Endpoints with no authentication
- User input passed directly to a query or system call

> ⚠️ LAB TASK: Add the things YOUR reviewer should never miss.
