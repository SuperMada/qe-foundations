# Pull request / branch checklist

Paste this into the description of your pull request (or tick it in a file if you use a
local bare remote). Every box must be ticked or have a one-line reason.

## Branch and history
- [x] Work is on a feature branch named `feature/sql-validation-<names>` (not `main`)
- [x] Branch is pushed; `git status` says "up to date with origin/..."
- [x] Both partners have commits under their own `user.name` (`git shortlog -sn`)
- [x] At least 6 commits, each with a message that says what changed and why
      (`Add R-03 status domain check`, not `update`)
- [x] Each partner has pulled (`git pull`) at least once during the session, and `git fetch` + `git log origin/<branch>` was used to look before pulling
- [x] No merge-conflict markers (`<<<<<<<`) anywhere; if there was a conflict, it was resolved by both partners
- [x] No generated files committed: `logs/`, `*.db`, `__pycache__/`

## The artifact
- [x] `sql/validation_queries.sql` has R-01..R-12, E-01, E-02; headers and `@expect` lines untouched
- [x] `python -m qe_foundations.validation` prints one PASS/FAIL line per rule and writes `logs/validation.log`
- [x] `ValidationFailedError` is raised for a failing rule and covered by a test
- [x] `python -m unittest qe_foundations.tests.test_validation` passes (>= 5 tests)
- [x] `python check_exercise.py` shows no FAIL
- [x] `qe_foundations/docs/`: `defect_checklist.md`, `defect_reports.md`, `pairing_log.md`, `retrospective.md` are complete

## Review (the OTHER partner ticks these after reading the diff)
- [x] I can explain every query in plain English
- [x] I ran the suite on my own machine after `git pull`
- [x] I found no secrets, passwords or personal data in the diff

## PR description (3 lines)
1. What this adds: This adds sql rules to make sure the database is following the correct design, python runner to run the rules and report the failures and logging
2. How to run it: python -m qe_foundations.validation
3. Known gaps / questions: N/A
