# Testing

Tests prove two things: the strict rules (invariants) in
[`ontology.md`](ontology.md) are true, and the behaviour a ticket promises
works. A test that can never fail proves nothing.

## Kinds of Tests

| Kind | Marker | What it uses | Use it for |
| :--- | :--- | :--- | :--- |
| Unit | none | Nothing outside the code | Simple functions, model methods that do not need a saved row |
| Database | `@pytest.mark.django_db` | A PostgreSQL test database | Models, constraints, services |
| View | `client` fixture (+ `django_db`) | A full request and response | URLs, views, templates, forms |

For features, use **view tests** first. They test URL → view → form → model →
template together. Most bugs in how the parts connect are found there.

pytest-django creates a separate database, `test_<POSTGRES_DB>`, and deletes it
after the tests. Your development data is never changed.

## Useful Fixtures

A fixture is something pytest prepares and gives to your test.

| Fixture | What you get |
| :--- | :--- |
| `client` | A Django test client (not logged in) |
| `admin_client` | A client logged in as a superuser |
| `db` | Access to the database in a test (same as the marker) |
| `settings` | Change a setting for one test only |
| `django_assert_num_queries` | Fails if some code runs more database queries than you expect (finds the N+1 problem) |

## Tests We Must Have

Each row needs at least one test. Tickets add new rows.

| # | Behaviour | Proves |
| :--- | :--- | :--- |
| T-1 | `/health/` returns `200 ok` and does not use the database | `TASK-001` AC-2 |
| T-2 | The test database works with the project settings | `TASK-001` AC-3 |
| T-3 | Two Posts with the same slug → `IntegrityError` | I-3, `TASK-004` AC-4 |
| T-4 | A published Post without a publish date → `IntegrityError` | I-4, `TASK-004` AC-5 |
| T-5 | A draft without a publish date can be saved | I-4 is not too strict |
| T-6 | `str(post)` is the title | `TASK-004` AC-6 |

## How to Write Tests

- One behaviour in each test. Use the behaviour as the name:
  `test_lent_book_cannot_be_borrowed`.
- Create the data inside the test (or in a fixture). Never use rows that
  another test created.
- Check the result you can see — a row, a status code, text on the page.
- Also test what happens when things go wrong: a bad form, an object that does
  not exist, an action that is not allowed.
- Code that depends on time: give the time to the code, or override it. Never
  use `time.sleep()`.

## Commands

```bash
docker compose exec web pytest
docker compose exec web pytest -k health           # only tests with this name
docker compose exec web pytest tests/test_health.py
docker compose exec web pytest -x --lf            # stop at the first failure, run only the last failed tests
```

## Before You Say Something Works

Run the tests and read the output. "It should pass" is not a result.
