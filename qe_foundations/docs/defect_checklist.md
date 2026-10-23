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
| R-01 | 5006, 5019, 5025 | 3 | as we predicted |
| R-02 | 5011, 5022 | 4 | we forgot we shouldnt get null |
| R-03 | 5008, 5014, 5027, 5029 | 2 | didnt realize we needed null and one of the status had spaces |
| R-04 | 5009, 5016 | 2 | as we predicted |
| R-05 | 5030, 5023 | 2 | as we predicted |
| R-06 | 5013, 5020 | 2 | as we predicted |
| R-07 | 5017, 5024, 5026 | 3 | as we predicted |
| R-08 | 5014, 5018, 5028 | 4 | hard to see whitespace in the printed version of the database |
| R-09 | 5010, 5015, 5035 | 2 | missed one, oops |
| R-10 | 5005, 5032 | 1 | missed a future date |
| R-11 | 5003, 5012, 5033 | 3 | as we predicted |
| R-12 | 5031, 5034, 5036, 5037 | 4 | as we predicted |

## Decoys: rows that look odd but are LEGAL (we must not flag them)

5042 SKIPPED with 0ms -- skipped tests take no time
5018 _test_search_basic -- whitespace before the start of the test name


## Rows reported by more than one rule

<!-- Which run_ids appear in two or more rules? Is that OK? (Each rule must be testable on its own.) -->
5014 is the only run_id that apears in 2 or more rules. This is ok for the rule checker becuase a row is possible of breaking more than one rule. If the row was tested for only one of them the row would pop up with either one.


## Open questions for the product owner

<!-- Rules that are really business decisions (like "is a price of 0 allowed?" in the lesson). -->
R-05 - It was a business decision to tag everything above 60000 needing review
R-07 - It was a business decision the names of the environments
R-12 - It was a business decision to make the format of build_id 'B-____'
