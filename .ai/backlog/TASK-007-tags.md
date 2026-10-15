# TASK-007 — Add Tags and a page for each Tag

| Field | Value |
| :--- | :--- |
| **Status** | `planned` |
| **Priority** | P1 (main feature) |
| **Value driver** | `V-5` from [`../business/VALUE.md`](../business/VALUE.md) |
| **Needs first** | `TASK-005` |
| **Created** | 2026-10-14 |

## Goal

An Author adds Tags to a Post. A Reader clicks a Tag and sees all published
Posts with that Tag.

## What You Will Learn

| Idea | Docs |
| :--- | :--- |
| `ManyToManyField` (many-to-many) | [Many-to-many](https://docs.djangoproject.com/en/5.2/topics/db/examples/many_to_many/) |
| Filtering across a connection: `Post.objects.filter(tags__slug=...)` | [Lookups that span relationships](https://docs.djangoproject.com/en/5.2/topics/db/queries/#lookups-that-span-relationships) |
| `ListView.get_queryset()` with a value from the URL | [Dynamic filtering](https://docs.djangoproject.com/en/5.2/topics/class-based-views/generic-display/#dynamic-filtering) |
| `filter_horizontal` in the admin | [ModelAdmin options](https://docs.djangoproject.com/en/5.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.filter_horizontal) |

## Ontology Links

**Ideas used:** Post, Tag.
**Strict rules that must stay true:** `I-1`.
**New ideas:** none.

## Acceptance Criteria

- [ ] AC-1 — In the admin you can create Tags and choose several Tags for a Post.
- [ ] AC-2 — The list page and the Post page show each Post's Tags as links.
- [ ] AC-3 — `/tags/<slug>/` lists only published Posts with that Tag (I-1).
      A test with a draft that has the Tag checks it.
- [ ] AC-4 — An unknown Tag slug returns `404`.
- [ ] AC-5 — The list page runs the same number of queries for 1 Post and for
      10 Posts (`django_assert_num_queries`).

## Not in This Ticket

Search, a tag cloud.
