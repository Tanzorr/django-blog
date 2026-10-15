# TASK-003 — Create a dev admin user with one command

| Field | Value |
| :--- | :--- |
| **Status** | `planned` |
| **Priority** | P2 (quality) |
| **Value driver** | `V-1` from [`../business/VALUE.md`](../business/VALUE.md) |
| **Needs first** | `TASK-001` |
| **Created** | 2026-10-14 |

## Goal

After a fresh clone, the owner runs one command and can log in at
`http://localhost:8000/admin/`. They do not need to type a username and
password by hand every time they reset the database.

## What You Will Learn

| Idea | Docs |
| :--- | :--- |
| Built-in migrations: the `auth` app already has migrations for the `User` table; `migrate` applies them | [Migrations](https://docs.djangoproject.com/en/5.2/topics/migrations/) |
| Superuser: a user with `is_staff` and `is_superuser`, who can open the admin | [createsuperuser](https://docs.djangoproject.com/en/5.2/ref/django-admin/#createsuperuser) |
| `createsuperuser --noinput` reads `DJANGO_SUPERUSER_*` env variables, so a script can run it | [Same page](https://docs.djangoproject.com/en/5.2/ref/django-admin/#createsuperuser) |
| `admin_client` fixture in pytest-django | [pytest-django helpers](https://pytest-django.readthedocs.io/en/latest/helpers.html#admin-client-django-test-client-logged-in-as-admin) |

## Ontology Links

**Ideas used:** none — `User` is Django's built-in model, not a domain idea.
**Strict rules that must stay true:** none yet (ontology is empty).
**New ideas:** none.

## Acceptance Criteria

- [ ] AC-1 — `.env.example` has `DJANGO_SUPERUSER_USERNAME`,
      `DJANGO_SUPERUSER_EMAIL` and `DJANGO_SUPERUSER_PASSWORD` with dev-only
      values. `docker-compose.yml` passes them to `web`, with defaults.
- [ ] AC-2 — `docker compose exec web python manage.py createsuperuser --noinput`
      creates the user with no questions.
- [ ] AC-3 — With that user, login at `/admin/` works and shows **Users** and
      **Groups**.
- [ ] AC-4 — The command is in [`../context/stack.md`](../context/stack.md),
      after `migrate`, as the "first run" steps.
- [ ] AC-5 — A test: `admin_client` gets `/admin/` → `200`. A second test:
      an anonymous `client` gets `/admin/` → `302` to the login page.
- [ ] AC-6 — No new migration. `makemigrations --check` finds nothing.

## Not in This Ticket

| Not here | Why |
| :--- | :--- |
| A new migration | `auth` migrations come with Django and are already applied. A data migration with a password would put the password in git and run it in every test database. |
| A custom `seed` management command | Write a new ticket if `--noinput` failing on a second run becomes a problem. |
| Seed data for Posts (fixtures) | No `Post` model before `TASK-004`. |
| A custom `User` model | We use the built-in one — ADR-008 in [`architecture.md`](../context/architecture.md). |

## Notes

- `createsuperuser --noinput` fails if the user already exists. This is OK:
  you run it once after a fresh database.
- The password is dev-only. Never use these values outside your computer.
