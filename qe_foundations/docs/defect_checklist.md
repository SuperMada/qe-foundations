# Expected-defect checklist (fill in as you go)

<!--
PURPOSE: this is your "answer sheet" for the data. Writing the PREDICTION before you run a
query is the single best habit for catching false passes.
HOW: for each rule, (1) write what you EXPECT in the "Predicted" column BEFORE running the
query, (2) run it, (3) write the run_ids it actually returned in "Defects found (run_ids)"
(comma-separated, 4-digit ids), (4) note anything surprising. Do not delete rows.
check_exercise.py compares this table with what your queries return.
-->

| Rule | Defects found (run_ids) | Predicted (before running) | Notes / surprises |
|---|---|---|---|
| R-01 | 3 | 3 | as we predicted |
| R-02 | 2 | 4 | we forgot we shouldnt get null |
| R-03 | 4 | 2 | didnt realize we needed null and one of the status had spaces |
| R-04 | 2 | 2 | as we predicted |
| R-05 | 2 | 2 | as we predicted |
| R-06 | 2 | 2 | as we predicted |
| R-07 | 3 | 3 | as we predicted |
| R-08 | 3 | 4 | hard to see whitespace in the printed version of the database |
| R-09 | 3 | 2 | missed one, oops |
| R-10 | 2 | 1 | missed a future date |
| R-11 | 3 | 3 | as we predicted |
| R-12 | 4 | 4 | as we predicted |

## Decoys: rows that look odd but are LEGAL (we must not flag them)

<!-- List at least two run_ids and say why they are fine, e.g. "run 5xxx: SKIPPED with 0 ms -- skipped tests take no time." -->


## Rows reported by more than one rule

<!-- Which run_ids appear in two or more rules? Is that OK? (Each rule must be testable on its own.) -->


## Open questions for the product owner

<!-- Rules that are really business decisions (like "is a price of 0 allowed?" in the lesson). -->

