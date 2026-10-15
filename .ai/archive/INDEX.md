# Archive

Finished tickets. A ticket moves here from [`../backlog/`](../backlog/INDEX.md)
when every point of its Definition of Done is true
([`../context/conventions.md`](../context/conventions.md)).

## Finished Tickets

| ID | Title | Finished | Goal | Result |
| :--- | :--- | :--- | :--- | :--- |
| [TASK-004](TASK-004-post-model-admin.md) | Add the `blog` app with the Post model and admin | 2026-10-15 | V-1 | `Post` model + admin; I-3 and I-4 enforced by the database and tested |
| [TASK-002](TASK-002-choose-domain.md) | Choose the domain; fill `VALUE.md` and `ontology.md` | 2026-10-14 | V-4 | Domain is a blog: 5 ideas, 5 strict rules, ADR-008, tickets TASK-004 – TASK-007 |
| [TASK-001](TASK-001-project-skeleton.md) | Basic Django + Docker Compose project | 2026-10-14 | V-3 | One command starts `web` + `db` and both are healthy; pytest, ruff and migrations checked inside the container |

## How to Move a Ticket Here

1. Fill in the ticket's **Result** section: what was built, changes from the
   plan, strict rules checked, new tickets (with their IDs).
2. Set `Status: done`.
3. `git mv .ai/backlog/TASK-NNN-*.md .ai/archive/`
4. Remove its row from the backlog table; add a row here.

## Why We Keep This

Six months later, the useful question is usually not "what does this code do?"
— the code itself answers that. The useful question is "what did we want to
achieve, and what ideas did we say no to?" The result notes answer this.

**Never change** a ticket in the archive. If its decision was wrong, write a new
ticket that links to it.
