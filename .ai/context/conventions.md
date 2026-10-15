# Code Rules

Rules for every line of code in this repository. When a rule has a reason, we
give the reason. If you understand why a rule exists, you can use it in cases
the rule does not mention.

## Language and Style

- **Python 3.12.** Every function has type hints.
- **PEP 8**, checked by `ruff format` and `ruff check`. Both must show no
  problems before you finish.
- Use f-strings to build text; use `pathlib.Path` for file paths.
- Use `TextChoices` / `IntegerChoices` when a value can only be one of a fixed
  list. Do not use plain strings for this.

## Names

| Thing | Rule | Example |
| :--- | :--- | :--- |
| Django app | short, lowercase, plural noun | `books` |
| Model | `CamelCase`, singular | `Book` |
| Field | `snake_case`; date+time ends in `_at`, date only ends in `_on` | `published_at` |
| Function / variable | `snake_case` | `mark_as_read()` |
| Service function | starts with a verb | `borrow_book(book, member)` |
| Constant | `UPPER_SNAKE` | `MAX_LOANS` |
| URL name | with the app name: `app:action` | `books:detail` |
| Template | `<app>/<model>_<action>.html` | `books/book_detail.html` |
| Migration | `--name` says what it does | `0002_add_isbn_to_book` |
| Test | `test_<behaviour>` | `test_borrowing_a_lent_book_is_refused` |

**Names come from the ontology.** If the ontology says `Book`, the model is not
called `Item` or `Product`.

## App Structure

```
<app>/
  models.py       Data + rules about one row
  services.py     Actions that use several models (create it when you first need it)
  views.py        Short and simple
  forms.py        Checks the data that users send
  urls.py         app_name = "<app>"
  admin.py        Register every model here
  templates/<app>/
  tests/          test_models.py, test_views.py, test_services.py
  migrations/     Committed to git, never changed after they are applied
```

## DO

- **Keep views short.** If a view calculates a business rule, the code is in
  the wrong place.
- **Register every model in the admin.** You get create/edit/delete pages for
  free, and it is the fastest way to see your data.
- **Use `get_object_or_404`** when you find an object by a value from the URL.
- **Put writes with several steps inside `transaction.atomic()`**, in the
  service. Then either all steps are saved, or none.
- **Use `select_related` / `prefetch_related`** when a template loops over
  related objects. Without them, Django runs one query for every row (the N+1
  problem).
- **Use `django.utils.timezone.now()`**, never `datetime.now()`. `USE_TZ = True`.
- **Add a `__str__` method** to every model. The admin and the shell use it.
- **Give migrations a name** with `--name`, and commit them together with the
  model change.

## DON'T

- **Don't change a migration that was already applied.** Write a new one.
- **Don't build SQL with f-strings.** Use the ORM, or parameters in `raw()`.
- **Don't use `|safe` or `mark_safe` on user data.** Templates escape HTML by
  default for a good reason (safety).
- **Don't put business logic in templates.**
- **Don't read `os.environ` outside `config/settings.py`** (ADR-003).
- **Don't use `null=True` on `CharField`/`TextField`.** For text, an empty
  string means "no value". Two different "empty" values cause bugs.
- **Don't leave `print()`, `breakpoint()` or code in comments** in a change.
- **Don't add a package to solve a five-line problem.** Ask before you add any
  dependency.
- **Don't commit `.env`** or real passwords and keys.

## Errors

- Object does not exist → `404`, with `get_object_or_404`.
- Form has bad data → show the form again with the errors, status `200`
  (Django's default), or `400` for JSON.
- Don't catch an exception if you cannot handle it. A bare `except:` hides bugs.

## Commits

- The first line is a command, 72 characters or less: `Add Book model and admin`.
- Name the ticket in the message body: `Ticket: TASK-003`.
- One logical change in each commit.

## Definition of Done

A ticket is finished only when all of this is true:

1. The code follows the rules above; `ruff check` and `ruff format --check`
   show no problems.
2. Tests cover the new behaviour, and also what happens when it fails.
3. All `pytest` tests pass.
4. `python manage.py makemigrations --check` finds no missing migrations.
5. Every strict rule (invariant) the change touches is still true. Write which
   ones in the ticket.
6. If you made a decision, it is written as an ADR in
   [`architecture.md`](architecture.md).
7. If you added or renamed an idea, [`ontology.md`](ontology.md) is updated.
8. A change that users can see has a line in
   [`CHANGELOG.md`](../../CHANGELOG.md) that starts with the ticket ID.
9. The ticket is moved to [`../archive/`](../archive/INDEX.md) with a note
   about the result.
