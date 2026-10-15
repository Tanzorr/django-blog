# Architecture

How the ontology becomes code. The ontology says what exists; this file says
where it lives in the code.

## Layers

```
HTTP                      urls.py, views.py, forms.py, templates/
   │                      Short and simple. Read the input, call a service, show the result.
   ▼
Services                  <app>/services.py
   │                      Business actions that use several models or
   │                      need a transaction. They call transaction.atomic().
   ▼
Models                    <app>/models.py
                          Data, constraints, and rules about one row
                          (methods, properties, Meta.constraints).
```

Rule: **a layer may use only the layers below it.** A model never imports a
view or a form. A template never decides a business rule.

A rule about **one object** goes on the model. A rule that works with
**several objects** goes in a service function. A view does neither.

## Project Folders

```
config/          The Django project: settings, main urls, wsgi/asgi
  views.py       Only project-level views (health check)
<app>/           One folder for each Django app, in the main project folder
tests/           Tests for the whole project (basic checks, health)
docker/web/      The web image
```

## Where Each Idea Lives in Code

You must be able to find every ontology idea in the code.

| Ontology idea | Lives in |
| :--- | :--- |
| Author | Django's built-in `User` (`django.contrib.auth`) — ADR-008 |
| Post | `blog/models.py` → `Post` (`TASK-004`) |
| Comment | `blog/models.py` → `Comment` (`TASK-006`) |
| Tag | `blog/models.py` → `Tag` (`TASK-007`) |
| Reader | Not saved. An anonymous visitor; `Comment.name` keeps their name |

## Architecture Decision Records (ADRs)

An ADR is a short note about a decision: what we chose, why, and what it costs
us. Each one has a date. When a decision changes, we edit its ADR here.

### ADR-001 — PostgreSQL, not SQLite
**2026-10-14 · Accepted**
SQLite is Django's default and needs no setup. But real Django projects use
PostgreSQL, and the two work differently in ways that cause problems later:
how strict data types are, `LIKE` with upper/lower case letters, many writes at
the same time, how constraints work. If we learn with the real database, we do
not need to unlearn things later. Cost: one more container, and you need
Docker.

### ADR-002 — `requirements.txt` with exact versions, no Poetry/uv
**2026-10-14 · Accepted**
One file, one `pip install`, nothing new to learn. The packages we use directly
have exact versions, so a rebuild next month installs the same versions. Cost:
the packages that our packages need are not fixed to exact versions, and
development tools (pytest, ruff) are in the same image as the app. This is OK
while nothing is deployed.

### ADR-003 — Settings read `os.environ` directly, no `django-environ`
**2026-10-14 · Accepted**
Three small helper lines in `settings.py` handle true/false values and lists.
A package for this is one more dependency to trust, for a five-line problem.
`os.environ` is read only in `config/settings.py`; all other code uses
`django.conf.settings`.

### ADR-004 — `runserver` in Compose, no gunicorn/nginx
**2026-10-14 · Accepted**
This is a development setup. `runserver` restarts by itself when you save a
file, and serves static files in debug mode. That is what we need for learning.
Cost: the setup is not like production. A future deployment ticket will add
gunicorn and a plan for static files.

### ADR-005 — Migrations do not run when the container starts
**2026-10-14 · Accepted**
If `migrate` runs when the container starts, a broken migration is hidden in a
container that keeps restarting. When you run it yourself, you see the output,
and you learn what a migration is. Cost: one command to run by hand after you
get new migrations.

### ADR-006 — pytest + pytest-django, not `manage.py test`
**2026-10-14 · Accepted**
Simple functions and `assert`, not `TestCase` classes and `self.assertEqual`.
Fixtures (`client`, `db`, `admin_client`), not `setUp`. Cost: two more
dependencies, and pytest-style tests do not run with `manage.py test` — use
only `pytest`.

### ADR-007 — ruff to check and format code
**2026-10-14 · Accepted**
One fast tool does the work of flake8, isort and black. Its settings are in
`pyproject.toml`. Cost: nothing important.

### ADR-008 — Author is Django's built-in `User`, not a custom user model
**2026-10-14 · Accepted**
The admin, login and `createsuperuser` work with it, and there is nothing new
to learn. An Author is a `User` with `is_staff=True`. Cost: Django's docs
recommend a custom user model at the start of a project, because switching
later is hard. If we ever need extra fields for an Author (bio, photo), we add
a separate `Profile` model with a `OneToOneField` to `User`.

### ADR-009 — Deleting an Author with Posts is blocked (`on_delete=PROTECT`)
**2026-10-15 · Accepted**
`Post.author` uses `PROTECT`: Django refuses to delete a `User` who still has
Posts. With `CASCADE`, deleting a User would silently delete all their Posts.
Cost: to remove an Author, you must first delete or move their Posts.
