# django-blog

A first Django project. The goal is to learn Django and Python in the same way
real projects are built: PostgreSQL, migrations, tests, Docker, and settings
that come from environment variables.

## What You Need

Docker with Compose v2. You do not need to install anything else on your
computer.

## How to Start

```bash
docker compose up -d --build                        # build and start web + db
docker compose exec web python manage.py migrate    # create the tables
docker compose exec web python manage.py createsuperuser
```

Open <http://localhost:8000/admin/> and log in.

## Commands You Use Every Day

| Task | Command |
| :--- | :--- |
| Run the tests | `docker compose exec web pytest` |
| Check the code style (lint) | `docker compose exec web ruff check .` |
| Format the code | `docker compose exec web ruff format .` |
| Create a new app | `docker compose exec web python manage.py startapp <name>` |
| Create a new migration | `docker compose exec web python manage.py makemigrations <app> --name <what_it_does>` |
| Open the Django shell | `docker compose exec web python manage.py shell` |
| See the logs | `docker compose logs -f web` |
| Stop everything | `docker compose down` (the database data stays) |

When you change the code, the server restarts by itself. When you change
`requirements.txt`, build again with `docker compose up -d --build`.

All details about the tools and versions: [`.ai/context/stack.md`](.ai/context/stack.md).

## What Is in This Repository

| Path | What it is |
| :--- | :--- |
| `config/` | The Django project: settings and main URLs |
| `blog/` | The blog app: models, admin, tests |
| `tests/` | Tests for the whole project |
| `docker/` | How the Docker image is built |
| [`.ai/`](.ai/README.md) | Project knowledge: goals, domain, rules, planned work |
| [`CLAUDE.md`](CLAUDE.md) | Start page for AI coding agents |

Work is planned as tickets in [`.ai/backlog/`](.ai/backlog/INDEX.md). The next
ticket is **TASK-005 — show published Posts on a list page and a detail page.**
