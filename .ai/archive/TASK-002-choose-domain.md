# TASK-002 — Choose the domain; fill `VALUE.md` and `ontology.md`

| Field | Value |
| :--- | :--- |
| **Status** | `done` |
| **Priority** | P0 |
| **Value driver** | V-4 |
| **Needs first** | TASK-001 |
| **Created** | 2026-10-14 |

## Goal

Decide what the app does. Then every later ticket has names and rules to
follow. No code changes.

## What You Will Learn

How to plan the domain before you write code:

- which things are entities (later they become models),
- how they are connected (later `ForeignKey` / `ManyToManyField`),
- which rules must always be true (later constraints and tests).

## Ontology Links

**New ideas:** all of them — this ticket writes the ontology.

## Acceptance Criteria

- [x] AC-1 — `VALUE.md` names the domain and adds at least one goal (value
      driver) for the domain.
- [x] AC-2 — `ontology.md` lists 3–6 ideas, how they are connected, and at
      least two strict rules (invariants).
- [x] AC-3 — Open question Q-1 has an answer and is removed.
- [x] AC-4 — The backlog has 3–5 new tickets. Each ticket is one Django lesson
      (for example: first model + admin → list/detail pages → create form →
      login).

## Not in This Ticket

Any code. The next tickets write the models.

## Notes

Good first domains are small and well known: a book library, a to-do list with
projects, a recipe box, a personal expense tracker, a blog. Choose one where
many things of one kind belong to one thing of another kind (many-to-one), for
example `Recipe` → `Ingredient`. That is the first connection worth learning.

---

## Result

**Finished on:** 2026-10-14
**What was built:** The domain is a blog. `ontology.md` has 5 ideas (Author,
Post, Comment, Tag, Reader), their connections and 5 strict rules (I-1 – I-5).
`VALUE.md` names the domain and adds goal V-5. `architecture.md` shows where
each idea will live in code.
**Changes from the plan:** Added ADR-008 (Author is Django's built-in `User`),
because the Author idea needed this decision. Q-1 is answered; new question
Q-2 (approve Comments?) is open.
**Strict rules checked:** none — no code yet.
**New tickets created:** `TASK-004`, `TASK-005`, `TASK-006`, `TASK-007`.
