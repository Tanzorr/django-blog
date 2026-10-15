# Tools, Versions and Services

## Software

| Part | Version | What it does |
| :--- | :--- | :--- |
| Python | 3.12 | The language (`python:3.12-slim` image) |
| Django | 5.2 LTS | Web framework: ORM, migrations, admin, templates |
| PostgreSQL | 16 | Database (ADR-001) |
| psycopg | 3.x | Lets Python talk to PostgreSQL |
| pytest + pytest-django | — | Runs the tests (ADR-006) |
| ruff | — | Checks and formats the code (ADR-007) |
| Docker Compose | v2 | Runs all services on your computer |

The exact versions are in [`../../requirements.txt`](../../requirements.txt).
If this table and that file are different, the file is correct.

## Services (docker-compose)

| Service | Port inside the container | Port on your computer | Notes |
| :--- | :--- | :--- | :--- |
| `web` | 8000 | 8000 | `manage.py runserver`, restarts by itself when code changes (ADR-004). The project folder is shared into the container at `/app` |
| `db` | 5432 | **54321** | Data is saved in the volume `pg-data`. The port is not 5432, so it does not conflict with a PostgreSQL already on your computer |

Both services have a **health check**. `web` waits until `db` is healthy, then
it starts.

### The `web` image

Built from `python:3.12-slim`. The packages from `requirements.txt` are
installed when the image is built. It runs as the user `appuser`, with the same
UID/GID as your user on the computer. So files it writes into the shared folder
(migrations, caches) belong to you, not to `root`.

**Did you change `requirements.txt`? Build again:** `docker compose up -d --build`.

## Environment Variables

They are read only in [`config/settings.py`](../../config/settings.py) and
nowhere else (ADR-003). Every variable has a default value for development in
`docker-compose.yml`, so you do not need a `.env` file.

| Variable | Example | Meaning |
| :--- | :--- | :--- |
| `DJANGO_SECRET_KEY` | `dev-insecure-change-me` | Secret key for signing. Required — without it, settings stop with a clear error |
| `DJANGO_DEBUG` | `true` | Shows debug pages and turns on auto-restart |
| `DJANGO_ALLOWED_HOSTS` | `localhost,127.0.0.1` | Host names, separated by commas |
| `POSTGRES_DB` | `app` | Database name (`db` and `web` both use it) |
| `POSTGRES_USER` / `POSTGRES_PASSWORD` | `django` / `secret` | Login data (only for development) |
| `POSTGRES_HOST` / `POSTGRES_PORT` | `db` / `5432` | Compose sets these for `web` |
| `USER_ID` / `GROUP_ID` | `1000` | Your UID/GID on the computer, used when the image is built |

## Commands

```bash
docker compose up -d --build                      # start everything
docker compose exec web python manage.py migrate  # apply migrations
docker compose exec web python manage.py createsuperuser
docker compose exec web python manage.py startapp <name>
docker compose exec web python manage.py makemigrations <app> --name <what_it_does>
docker compose exec web python manage.py shell
docker compose exec web pytest
docker compose exec web ruff check .
docker compose exec web ruff format .
docker compose logs -f web
docker compose exec db psql -U django -d app     # SQL prompt
```

| URL | What |
| :--- | :--- |
| <http://localhost:8000/admin/> | Django admin |
| <http://localhost:8000/health/> | Shows that the app is running, returns `ok` |
