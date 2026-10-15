# Business Value

Why this project exists. Every ticket in [`../backlog/`](../backlog/INDEX.md)
links to one goal (value driver) on this page.

## 1. The Problem

The owner wants to learn Django and Python. Tutorials teach the syntax, but
each piece alone. They skip what a real project needs: a real database,
migrations, tests, settings from environment variables, and a development setup
that works the same on every computer.

## 2. The Idea

**One small but real app, built the same way as real Django projects.**
Every feature is a lesson. Every lesson comes with a test.

**The app is a blog.** It is small, everybody knows how it works, and it has
the connections worth learning first: one-to-many (Author → Post → Comment) and
many-to-many (Post ↔ Tag). The domain is in
[`../context/ontology.md`](../context/ontology.md).

## 3. Goals (Value Drivers)

| ID | Goal | How we reach it |
| :--- | :--- | :--- |
| **V-1** | Learn the Django basics: models, migrations, admin, views, URLs, templates, forms | The `blog` app, from `TASK-004` on |
| **V-2** | Learn to write good, normal Python: type hints, data structures, modules, exceptions | Code that passes `ruff` and review |
| **V-3** | Learn the habits of real projects: tests, Docker, settings from env variables, small commits | The `TASK-001` base project, [`../context/testing.md`](../context/testing.md) |
| **V-4** | A working app the owner can show to others and grow | The blog |
| **V-5** | Readers can read published posts by topic and leave comments | `TASK-005` – `TASK-007` |

## 4. How We Know It Works

- **S-1** — After a fresh `git clone`, `docker compose up -d --build` runs the
  project. The computer needs only Docker, nothing else.
- **S-2** — `pytest` and `ruff` pass on every commit.
- **S-3** — The owner can explain, in their own words, every Django feature the
  project uses.

## 5. What This Project Is Not

- **Not** a real production deployment. No gunicorn, nginx, HTTPS or CI until
  a ticket asks for them.
- **Not** a frontend framework project. We use Django templates. No React or
  Vue build step.
- **Not** an API-first project. Django REST Framework only if a ticket really
  needs it.
