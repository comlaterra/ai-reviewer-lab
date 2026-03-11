# CLAUDE.md

This file defines how AI tools should behave in this codebase.
Read this before writing, reviewing, or modifying any code.

---

## Architecture

This is a REST API built with Flask and SQLite.

The codebase follows a layered architecture:

- `src/api/` — Route handlers. Responsible for request parsing, validation, and response formatting.
- `src/services/` — Business logic. Database access, payment processing, referral system.
- `src/auth.py` — Authentication and authorization decorators.
- `src/models.py` — Database connection management and schema.
- `src/config.py` — Environment-based configuration.
- `src/utils.py` — Shared validators and helpers.

> LAB TASK: Is this actually true of the code you see? What is missing from this description?

---

## Hard Rules

- Never put secrets or credentials in source code. Use environment variables.
- Every endpoint must validate input before passing it to a service function.
- Errors returned to the client must never include internal stack traces or raw exception messages.

> LAB TASK: Add 2 or 3 rules specific to YOUR real codebase here.
> Think about the mistakes your team makes repeatedly.

---

## Auth

All endpoints that access or modify user data must use the `@require_auth` decorator.
Admin endpoints must additionally use `@require_role("admin")`.
Public endpoints (registration, health check) are the only exceptions.

> LAB TASK: Does the code actually follow this policy? What should the AI flag if it doesn't?

---

## Never Do This

- Raw SQL string formatting (use parameterised queries always)
- Catching exceptions and swallowing them silently

> LAB TASK: What else belongs here for your stack?

---

## Payments

Any code that touches `services/payments.py` or `api/payments.py` is high risk.
Treat it with extra scrutiny. Flag anything that moves money without an audit trail.

---

## What the AI Should Flag Immediately

- Hardcoded strings that look like API keys, tokens, or passwords
- Endpoints with no authentication
- User input passed directly to a query or system call
- Sensitive data (passwords, tokens) returned in API responses

> LAB TASK: Add the things YOUR reviewer should never miss.
