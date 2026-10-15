# Ontology

The main description of the domain. This file is always correct about the
domain. It says what exists and how the ideas are connected. It says nothing
about Django, tables or classes — that is in [`architecture.md`](architecture.md).

**Domain: a blog.** Authors write posts. Readers read the published posts and
leave comments.

---

## 1. Main Ideas

| Idea | Saved in the database | What it is in the domain |
| :--- | :--- | :--- |
| **Author** | yes | A person who writes Posts. Authors log in. |
| **Post** | yes | An article: title, text, a short URL name (slug), and a status: *draft* or *published*. A published Post has a publish date. |
| **Comment** | yes | A short text that a Reader writes under one Post, with the Reader's name and the date. |
| **Tag** | yes | A word that groups Posts by topic, for example `python`. |
| **Reader** | no | Anyone who visits the blog. Readers do not log in. |

## 2. Connections

```
Author   --writes-->      Post      (one Author, many Posts)
Post     --has-->         Comment   (one Post, many Comments)
Post     --is tagged-->   Tag       (many Posts, many Tags)
Reader   --writes-->      Comment   (the Reader is not saved; only their name is)
```

## 3. Strict Rules (Invariants)

Things that must always be true. If the code breaks one, it is a bug.

| # | Rule |
| :--- | :--- |
| I-1 | A Reader sees only published Posts. A draft is visible only to Authors. |
| I-2 | Every Post has exactly one Author. |
| I-3 | Every Post has a slug, and no two Posts have the same slug. |
| I-4 | A published Post always has a publish date. |
| I-5 | Every Comment belongs to exactly one Post. A Reader can comment only on a published Post. |

## 4. Open Questions

We write questions here; we do not answer them quietly. Each one becomes a
ticket when it becomes important.

- **Q-2** — Must an Author approve a Comment before Readers see it? For now:
  no, Comments show at once, and an Author can delete one in the admin.
