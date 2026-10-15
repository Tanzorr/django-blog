# TASK-004 — Add the `blog` app with the Post model and admin

| Field | Value |
| :--- | :--- |
| **Status** | `done` |
| **Priority** | P1 (main feature) |
| **Value driver** | `V-1` from [`../business/VALUE.md`](../business/VALUE.md) |
| **Needs first** | `TASK-002` |
| **Created** | 2026-10-14 |

## Goal

An Author logs in to the admin and can create, edit and delete Posts, as a
draft or published.

## What You Will Learn

| Idea | Docs |
| :--- | :--- |
| App, `startapp`, `INSTALLED_APPS` | [Applications](https://docs.djangoproject.com/en/5.2/ref/applications/) |
| Model fields: `CharField`, `SlugField`, `TextField`, `DateTimeField` | [Model fields](https://docs.djangoproject.com/en/5.2/ref/models/fields/) |
| `ForeignKey` to `User` (many-to-one) | [Many-to-one](https://docs.djangoproject.com/en/5.2/topics/db/examples/many_to_one/) |
| `TextChoices` for the status | [Enumeration types](https://docs.djangoproject.com/en/5.2/ref/models/fields/#enumeration-types) |
| `makemigrations` / `migrate` | [Migrations](https://docs.djangoproject.com/en/5.2/topics/migrations/) |
| `Meta.constraints` (`CheckConstraint`) | [Constraints](https://docs.djangoproject.com/en/5.2/ref/models/constraints/) |
| `ModelAdmin`: `list_display`, `list_filter`, `prepopulated_fields` | [The admin](https://docs.djangoproject.com/en/5.2/ref/contrib/admin/) |

## Ontology Links

**Ideas used:** Author, Post.
**Strict rules that must stay true:** `I-2`, `I-3`, `I-4`.
**New ideas:** none.

## Acceptance Criteria

- [x] AC-1 — `/admin/` shows **Posts**. You can create a Post with title,
      slug, text, status and Author.
- [x] AC-2 — The slug fills itself from the title while you type.
- [x] AC-3 — The Post list in the admin shows title, status, Author and publish
      date, and you can filter by status.
- [x] AC-4 — Two Posts with the same slug → error (I-3). A test checks it.
- [x] AC-5 — A published Post without a publish date → database error (I-4).
      A test checks it.
- [x] AC-6 — `str(post)` is the title.
- [x] AC-7 — The migration has a name (`--name add_post`) and is committed.

## Not in This Ticket

| Not here | Ticket |
| :--- | :--- |
| Pages for Readers | `TASK-005` |
| Comments | `TASK-006` |
| Tags | `TASK-007` |

---

## Result

**Finished on:** 2026-10-15
**What was built:** `blog` app; `Post` model (title, slug, author, body,
status, published_at, created_at); `PostAdmin` with columns, status filter,
search and slug prefill; migrations `0001_add_post` and
`0002_add_published_post_has_published_at`; 4 tests in
`blog/tests/test_models.py` (T-3 – T-6 in `testing.md`).
**Changes from the plan:** none. Added ADR-009 for `on_delete=PROTECT`.
**Strict rules checked:** I-2 (`author` is a required `ForeignKey`), I-3
(`slug` is `unique`, T-3), I-4 (`CheckConstraint`, T-4 and T-5).
**New tickets created:** none.
