# Changelog

Important changes. The newest changes are at the top. Each line names its
ticket, so you can find the ticket's acceptance criteria in
[`.ai/archive/`](.ai/archive/INDEX.md).

The format follows [Keep a Changelog](https://keepachangelog.com/). Adding a
line here is part of the Definition of Done in
[`.ai/context/conventions.md`](.ai/context/conventions.md).

## Unreleased

**Added**
- TASK-004: The `blog` app with the `Post` model. In the admin you can create,
  edit and delete Posts, filter them by status, and search by title. The slug
  fills itself from the title. The database refuses two Posts with the same
  slug, and a published Post without a publish date.
- TASK-001: Basic Django 5.2 + PostgreSQL 16 project in Docker Compose. Two
  services, `web` and `db`, both with health checks. One command starts
  everything: `docker compose up -d --build`. A `/health/` page that shows the
  app is running, the Django admin at `/admin/`, and pytest-django and ruff set
  up in `pyproject.toml`.
- The `.ai/` folder with project knowledge: business value, ontology (empty
  until TASK-002), context files, modes for the agent, backlog and archive.
- `CLAUDE.md` start page, with rules for the agent in a learning project.
- `.claude/settings.json` permission rules: the agent can read most things,
  must ask before it changes things, and cannot read secrets or run commands
  that delete data.
- `.editorconfig`, `.gitignore`, `.gitattributes`, `.env.example`.

---

## Rules for This File

- One line for each change that a user can see. Start it with the ticket:
  `TASK-003: …`.
- Write for a person who did not do the work.
- Sections: **Added**, **Changed**, **Fixed**, **Removed**.
