# TASK-006 — Let Readers comment on a Post

| Field | Value |
| :--- | :--- |
| **Status** | `planned` |
| **Priority** | P1 (main feature) |
| **Value driver** | `V-5` from [`../business/VALUE.md`](../business/VALUE.md) |
| **Needs first** | `TASK-005` |
| **Created** | 2026-10-14 |

## Goal

Under a published Post, a Reader types their name and a comment, sends the
form, and sees the comment on the page.

## What You Will Learn

| Idea | Docs |
| :--- | :--- |
| A second model with a `ForeignKey`, `related_name`, `on_delete` | [ForeignKey](https://docs.djangoproject.com/en/5.2/ref/models/fields/#foreignkey) |
| `ModelForm` | [ModelForms](https://docs.djangoproject.com/en/5.2/topics/forms/modelforms/) |
| GET vs POST, `{% csrf_token %}` | [Forms](https://docs.djangoproject.com/en/5.2/topics/forms/), [CSRF](https://docs.djangoproject.com/en/5.2/ref/csrf/) |
| Redirect after POST | [`redirect()`](https://docs.djangoproject.com/en/5.2/topics/http/shortcuts/#redirect) |
| Showing form errors | [Rendering fields](https://docs.djangoproject.com/en/5.2/topics/forms/#rendering-fields-manually) |
| `prefetch_related` | [QuerySet API](https://docs.djangoproject.com/en/5.2/ref/models/querysets/#prefetch-related) |
| `TabularInline` in the admin | [Inlines](https://docs.djangoproject.com/en/5.2/ref/contrib/admin/#inlinemodeladmin-objects) |

## Ontology Links

**Ideas used:** Post, Comment, Reader.
**Strict rules that must stay true:** `I-1`, `I-5`.
**New ideas:** none.

## Acceptance Criteria

- [ ] AC-1 — The Post page shows its Comments, oldest first, with name and date.
- [ ] AC-2 — A Reader sends name + text → redirect to the same page → the
      Comment is there.
- [ ] AC-3 — Empty name or text → the form shows again with errors, status
      `200`, nothing saved. A test checks it.
- [ ] AC-4 — A POST to a draft's comment URL → `404`, nothing saved (I-5).
      A test checks it.
- [ ] AC-5 — In the admin, a Post's page lists its Comments, and you can
      delete one.

## Not in This Ticket

| Not here | Ticket |
| :--- | :--- |
| Approving Comments before they show | Open question `Q-2` |
| Spam protection | A later ticket |
