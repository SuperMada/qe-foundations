# Defect reports (top 2 findings)

<!--
HOW TO USE: copy this file to  qe_foundations/docs/defect_reports.md.
Choose the TWO most serious defect groups your suite found (think: money, customers,
automation reliability). Write each as a real bug report using the structure from the
lesson "Using SQL for QA Data Validation", section "Reporting what you find".
Keep the "Title:" labels (the check script counts them) and paste the exact SQL.
-->

## Defect report 1

**Title:** R-02

**Rule:** R-02 Validity executed_by, when present, must look like an e-mail

**Environment / when:** test_runs.db, test_runs_seed.sql, 22/10/2026

**Query:**

```sql
SELECT run_id, executed_by
FROM test_runs
WHERE executed_by is not NULL and not TRIM(executed_by) like "" and executed_by not like "%@%.%" 
```

**Evidence:** (5011, 'priya.nair'), (5022, 'tom@qa')

**Impact:** The team must be able to trust these results because the team needs to be able to reach whoever ran the tests that are connected to the email and if the email doesn't exist they won't be able to find who ran the tests

**Severity (suggested) and why:** URGENT, because these emails don't exist and if someone trys to pull the emails and directly email each value in the column the email would be sent to no one and lost.

**Question or false-alarm check:** This would not be a defect if the exectued_by column does not have to be an email, as long as these are identifyers for employees they could still link the test runs back to a unique employee. This would be confirmed by a manager who decides what should be placed in executed_by


## Defect report 2

**Title:** R-12

**Rule:** R-12 Validity build_id must be present and look like B-1042 (upper-case 'B', dash, 4 characters)

**Environment / when:** test_runs.db, test_runs_seed.sql, 22/10/2026

**Query:**

```sql
SELECT run_id, build_id
FROM test_runs
WHERE build_id is Null or not upper(build_id) = build_id or not build_id like "B-____"
```

**Evidence:** (5031, 'B-12'), (5034, 'b-1048'), (5036, None), (5037, 'B1043')

**Impact:** The team must be able to trust the column build_id because they need to be able to link the builds in the database to test runs completed on the software to check if there was an error and go back to the test logs to find what went wrong

**Severity (suggested) and why:** URGENT, Without proper build_id the team would not be able to find the tests which led to the problem and will have to scroll the entire test logs to find the correct test logs

**Question or false-alarm check:** This would not be a defect if the build_id format was changed and needed to be updated in the rules. This could also not be an error if the build_id format is more of a guideline that won't normally link right back to the builds. This would be confirmed by a manager who decides what should be placed in build_id
