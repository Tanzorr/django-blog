# TASK-001 — Basic Django + Docker Compose project

| Field | Value |
| :--- | :--- |
| **Status** | `done` |
| **Priority** | P0 |
| **Value driver** | V-3 |
| **Needs first** | — |
| **Created** | 2026-10-14 |

## Goal

Clone the repository, run one command, and open a working Django admin that
uses PostgreSQL. Tests and the code checker (linter) must be ready before we
write the first line of domain code.

## What You Will Learn

Django project vs Django app ([docs](https://docs.djangoproject.com/en/5.2/intro/tutorial01/)),
`settings.py`, URLconf (the list of URLs), migrations, the admin, pytest-django.

## Acceptance Criteria

- [x] AC-1 — `docker compose up -d --build` starts `web` and `db`;
      `docker compose ps` shows both as healthy.
- [x] AC-2 — `http://localhost:8000/health/` returns `200 ok` and does not use
      the database.
- [x] AC-3 — `python manage.py migrate` works with `db`.
- [x] AC-4 — `http://localhost:8000/admin/` shows the login page.
- [x] AC-5 — `pytest`, `ruff check`, `ruff format --check`, `manage.py check`
      and `makemigrations --check` all pass.
- [x] AC-6 — Every env variable has a default value in `docker-compose.yml`;
      git ignores `.env`.
- [x] AC-7 — Files that the container writes into the shared project folder
      belong to your user on the computer (not to `root`).
- [x] AC-8 — A fresh clone needs only Docker on the computer, nothing else.

## Not in This Ticket

Any domain app — `TASK-002` chooses the domain first.

---

## Result

**Finished on:** 2026-10-14
**What was built:** the `config/` project (`settings.py` that reads env
variables, a `/health/` view, the admin URL), `docker/web/Dockerfile`
(`python:3.12-slim`, a user `appuser` with the same UID as your computer user,
packages installed inside the image), `docker-compose.yml` (`web` + `db` with
health checks), `requirements.txt` with exact versions, `pyproject.toml`
(pytest + ruff settings), `tests/test_health.py` (T-1, T-2).
**Changes from the plan:**
- We added `/health/` and did not use Django's welcome page. The welcome page
  shows only while `admin/` is the only URL, so it is not a stable page for a
  health check.
- `.claude/settings.json` blocks `.env`, `.env.local`, `.env.*.local` and
  `.env.production` — but not `.env.*`. That pattern would also block
  `.env.example`, and agents must be able to read that file.
- `ruff format --check .` complains about `demo1.py`, which was there before
  (the owner's Python exercise, not part of this ticket). We did not change it.
**Checked:** all checks ran inside the container — 2 tests passed, `ruff check`
found no problems, no missing migrations, `/health/` and `/admin/` return
`200`, both services `healthy`, `.pytest_cache`/`.ruff_cache` belong to
uid 1000.
**New tickets created:** `TASK-002`.
