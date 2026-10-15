# Mode: REVIEW

Check a change before it is committed. Does it do what the project promised?

## Read

1. The diff — `git diff`, or `git diff --staged`
2. The ticket that the change is for
3. [`../context/conventions.md`](../context/conventions.md) — the DON'T list and the Definition of Done
4. [`../context/ontology.md`](../context/ontology.md) — the strict rules (invariants)

## Checklist

**Does it work correctly?**
- Are all acceptance criteria done, or only most of them?
- Which strict rules (invariants) does the change touch? Is each one still true?
- What happens when things go wrong: bad input, an object that does not exist,
  a form sent two times, an empty list?

**Django**
- Are the migrations included, with a good name, and do they match the model
  change?
- Is there business logic in a view or a template? (It should not be there.)
- Does a list page run one extra query for every row (the N+1 problem)? Use
  `select_related` / `prefetch_related`.
- Is user data passed through `|safe` or `mark_safe`? (Dangerous.)
- Do forms check the data on the server, not only with HTML attributes?

**Size of the change**
- Does it do what the ticket says, and nothing more?
- Does it break a "this project is not" rule in
  [`../business/VALUE.md`](../business/VALUE.md)?

**Tests**
- Is there a test for the new behaviour *and* for the case when it fails?
- Would the test fail if someone broke the behaviour later?

**Rules for code**
- Type hints, names from the ontology, `os.environ` only in settings.
- No `print()`, no `breakpoint()`, no code in comments.

## Report

List the problems from the most serious to the least serious. For each one:

- **What** is wrong — one sentence.
- **Where** — `file.py:line`.
- **Why it matters** — what exactly goes wrong. If you cannot name an input
  that breaks it, call it a preference.

If a change is good, say so clearly. Keep problems that block the commit
separate from suggestions.

## Rules

- **Review the diff, not the whole file.** Old problems need their own tickets.
- **Check what people say.** If the ticket says the tests pass, run them.
- **Do not fix things while you review.**
