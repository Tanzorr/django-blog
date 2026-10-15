# TASK-005 — Show published Posts on a list page and a detail page

| Field | Value |
| :--- | :--- |
| **Status** | `planned` |
| **Priority** | P1 (main feature) |
| **Value driver** | `V-5` from [`../business/VALUE.md`](../business/VALUE.md) |
| **Needs first** | `TASK-004` |
| **Created** | 2026-10-14 |

## Goal

A Reader opens `http://localhost:8000/`, sees the newest published Posts, and
clicks one to read it.

## What You Will Learn

| Idea | Docs |
| :--- | :--- |
| URLconf with `app_name` and `include()` | [URL dispatcher](https://docs.djangoproject.com/en/5.2/topics/http/urls/) |
| `ListView` and `DetailView` | [Generic display views](https://docs.djangoproject.com/en/5.2/ref/class-based-views/generic-display/) |
| Templates: `{% extends %}`, `{% block %}`, `{% for %}`, `{% url %}` | [Template language](https://docs.djangoproject.com/en/5.2/ref/templates/language/) |
| A custom manager or `QuerySet` method: `Post.objects.published()` | [Managers](https://docs.djangoproject.com/en/5.2/topics/db/managers/) |
| `get_absolute_url` | [Model methods](https://docs.djangoproject.com/en/5.2/ref/models/instances/#get-absolute-url) |
| `select_related` (avoid N+1 queries) | [QuerySet API](https://docs.djangoproject.com/en/5.2/ref/models/querysets/#select-related) |

## Ontology Links

**Ideas used:** Post, Author, Reader.
**Strict rules that must stay true:** `I-1`.
**New ideas:** none.

## Acceptance Criteria

- [ ] AC-1 — `/` lists published Posts, newest first: title, Author, date.
- [ ] AC-2 — `/posts/<slug>/` shows one Post with its full text.
- [ ] AC-3 — A draft is not on the list, and its detail URL returns `404`
      (I-1). Tests check both.
- [ ] AC-4 — An unknown slug returns `404`. A test checks it.
- [ ] AC-5 — All pages use one `base.html` with the blog title and a link to `/`.
- [ ] AC-6 — Templates use `{% url %}`, never a written path like `"/posts/"`.

## Not in This Ticket

| Not here | Ticket |
| :--- | :--- |
| Pagination, CSS | A later ticket |
| Comments under the Post | `TASK-006` |
