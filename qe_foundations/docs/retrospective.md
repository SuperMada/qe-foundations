# Retrospective -- Thursday pair exercise (SQL validation)

<!--
HOW TO USE: copy this file to  qe_foundations/docs/retrospective.md  and answer every
"##" section below (keep the headings). Write TOGETHER in the last 15 minutes; both
partners must agree with what is written. Aim for 2-4 specific sentences per section
(about 250-400 words in total). "It went well" is not an answer: name a rule, a
moment, a query, a commit.
Delete nothing except these comments.
-->

## Pair and branch

<!-- Names of both partners, the repo + branch you worked on, the final commit hash. -->
Adam Fischer & Philo Girgis, https://github.com/SuperMada/qe-foundations, https://github.com/SuperMada/qe-foundations/tree/feature/sql-validation-Adam-Fischer-Philo-Girgis, 989dae2


## What we built

<!-- In your own words: what is in the repo now (queries, runner, tests, docs)? How many rules did your suite end with, and what does one `python -m qe_foundations.validation` run print? -->
The repo contains the new sql queries along with a runner to run all the rules and check that they evalutate how we want them to. It also includes the test cases we ran to make sure the rules work properly and exceptions are raised properly. The suite ended with 12 rules. 

2026-10-23 13:09:05,922 - WARNING - FAIL: R-01 Completeness executed_by must be present (not NULL, not blank) (3 violating row(s))
FAIL  R-01  Completeness  executed_by must be present (not NULL, not blank)  (3 violating row(s))
      (5006, None)
      (5019, '')
      (5025, '   ')
2026-10-23 13:09:05,933 - WARNING - FAIL: R-02 Validity executed_by, when present, must look like an e-mail (contain '@' and a '.' after it) (2 violating row(s))
FAIL  R-02  Validity  executed_by, when present, must look like an e-mail (contain '@' and a '.' after it)  (2 violating row(s))
      (5011, 'priya.nair')
      (5022, 'tom@qa')
2026-10-23 13:09:05,936 - WARNING - FAIL: R-03 Validity status must be exactly PASSED, FAILED, SKIPPED or ERROR (upper case) (4 violating row(s))
FAIL  R-03  Validity  status must be exactly PASSED, FAILED, SKIPPED or ERROR (upper case)  (4 violating row(s))
      (5008, 'Passed')
      (5014, 'FAILED ')
      (5027, None)
      (5029, 'PASS')
2026-10-23 13:09:05,938 - WARNING - FAIL: R-04 Validity duration_ms must be present and not negative (0 is legal, e.g. SKIPPED) (2 violating row(s))
FAIL  R-04  Validity  duration_ms must be present and not negative (0 is legal, e.g. SKIPPED)  (2 violating row(s))
      (5009, -250)
      (5016, None)
2026-10-23 13:09:05,938 - WARNING - FAIL: R-05 Accuracy duration_ms above 600000 (10 minutes) is an outlier needing review (2 violating row(s))
FAIL  R-05  Accuracy  duration_ms above 600000 (10 minutes) is an outlier needing review  (2 violating row(s))
      (5030, 7200000)
      (5023, 900000)
2026-10-23 13:09:05,939 - WARNING - FAIL: R-06 Validity retries must be present and between 0 and 3 inclusive (2 violating row(s))
FAIL  R-06  Validity  retries must be present and between 0 and 3 inclusive  (2 violating row(s))
      (5013, -1)
      (5020, 7)
2026-10-23 13:09:05,940 - WARNING - FAIL: R-07 Validity environment must be exactly DEV, QA or STAGING (3 violating row(s))
FAIL  R-07  Validity  environment must be exactly DEV, QA or STAGING  (3 violating row(s))
      (5017, 'PROD')
      (5024, 'qa')
      (5026, None)
2026-10-23 13:09:05,943 - WARNING - FAIL: R-08 Consistency test_name, suite and status must have no leading/trailing spaces (3 violating row(s))
FAIL  R-08  Consistency  test_name, suite and status must have no leading/trailing spaces  (3 violating row(s))
      (5014, 'test_api_rate_limit', 'API', 'FAILED ')
      (5018, ' test_search_basic', 'SMOKE', 'PASSED')
      (5028, 'test_login_bad_password', 'SMOKE ', 'PASSED')
2026-10-23 13:09:05,944 - WARNING - FAIL: R-09 Validity started_at and finished_at must be present and shaped 'YYYY-MM-DD HH:MM:SS' (3 violating row(s))
FAIL  R-09  Validity  started_at and finished_at must be present and shaped 'YYYY-MM-DD HH:MM:SS'  (3 violating row(s))
      (5010, '03/04/2025 10:15', '2025-04-03 10:15:09')
      (5015, '2025-04-07 14:30:00', '2025-04-07T14:30:12')
      (5035, '2025-04-16 09:30:00', None)
2026-10-23 13:09:05,946 - WARNING - FAIL: R-10 Consistency a run cannot finish before it starts, and cannot start in the future (2 violating row(s))
FAIL  R-10  Consistency  a run cannot finish before it starts, and cannot start in the future  (2 violating row(s))
      (5005, '2025-04-02 09:15:00', '2025-04-02 09:14:50')
      (5032, '2099-01-01 08:00:00', '2099-01-01 08:00:05')
2026-10-23 13:09:05,946 - WARNING - FAIL: R-11 Consistency FAILED/ERROR runs need a failure_message; PASSED runs must not have one (3 violating row(s))
FAIL  R-11  Consistency  FAILED/ERROR runs need a failure_message; PASSED runs must not have one  (3 violating row(s))
      (5003, 'FAILED', None)
      (5012, 'PASSED', 'Warning: slow response on first call')
      (5033, 'ERROR', '')
2026-10-23 13:09:05,948 - WARNING - FAIL: R-12 Validity build_id must be present and look like B-1042 (upper-case 'B', dash, 4 characters) (4 violating row(s))
FAIL  R-12  Validity  build_id must be present and look like B-1042 (upper-case 'B', dash, 4 characters)  (4 violating row(s))
      (5031, 'B-12')
      (5034, 'b-1048')
      (5036, None)
      (5037, 'B1043')
2026-10-23 13:09:05,949 - INFO - PASS: E-01 Expectation run 5001 was saved as expected (test_login_valid_user, SMOKE, QA, PASSED, build B-1042)
PASS  E-01  Expectation  run 5001 was saved as expected (test_login_valid_user, SMOKE, QA, PASSED, build B-1042)
2026-10-23 13:09:05,950 - INFO - PASS: E-02 Expectation test-data discovery: the most recent FAILED run in QA exists (exactly one row returned)
PASS  E-02  Expectation  test-data discovery: the most recent FAILED run in QA exists (exactly one row returned)


## How the pairing worked

<!-- Did the driver/navigator split and the 30-minute swaps work? Give one concrete moment where the navigator caught something the driver would have missed, and one moment the pairing felt awkward or slow. What did you change as a result? -->
Yes as a driver navigator pair we swapped just about every 30mins. One moment the navigator caught something that the driver would have missed was while writing the sql queries often the driver would trip up on if we wanted to get the result or 'not' the result and the navigator would correct what they wrote. One moment the pairing felt akward was during the coding of the logger and neither team member had much experiance with creating loggers before and so the driver and navigator both had trouble figuring out what needed to be done. The change as a result of it was to have the navigator look ahead to research upcoming coding needs to figure out what needed to be done while the driver coded the simple things they could without extra navigator help.


## The hardest rule

<!-- Which rule (R-xx) took longest, and why? Quote the first wrong version of the query and what it returned (too many rows? none? an error?), then what fixed it. -->

R-11 took the longest because we didn't realise that we misspelled error.

SELECT run_id, status, failure_message
FROM test_runs
WHERE status in ("FAILED", "ERRROR") and failure_message is Null or status like "PASSED" and failure_message is not Null

R-11 | Consistency | FAILED/ERROR runs need a failure_message; PASSED runs must not have one
  run_id | status | failure_message                     
  -------+--------+-------------------------------------
  5003   | FAILED | NULL                                
  5012   | PASSED | Warning: slow response on first call
  (2 row(s))

SELECT run_id, status, failure_message
FROM test_runs
WHERE status in ("FAILED", "ERROR") and (failure_message is Null or trim(failure_message) like "") or status like "PASSED" and failure_message is not Null

R-11 | Consistency | FAILED/ERROR runs need a failure_message; PASSED runs must not have one
  run_id | status | failure_message                     
  -------+--------+-------------------------------------
  5003   | FAILED | NULL                                
  5012   | PASSED | Warning: slow response on first call
  5033   | ERROR  |                                     
  (3 row(s))


## A surprise in the data

<!-- Which defect did you NOT expect, or which "defect" turned out to be a legitimate row (a false alarm you avoided or briefly fell for)? What would you ask the product owner about it? -->
Did not expect 5034 to be a defect for having a lowercase B
I would ask the product owner if the capitals are really necessary


## SQLite and SQL pitfalls we hit

<!-- NULL behaviour, case sensitivity of = / IN versus LIKE, trailing spaces, inclusive BETWEEN, AND/OR precedence... Which of these bit you, and how will you spot it next time? -->
We didn't realize that in would pass over Null behavior.
We will ensure to check Null seperately in the future


## Skills we connected from this week

<!-- Name one thing each from Monday (modules/venv/Git), Tuesday (exceptions/files), Wednesday (logging/unittest/merge conflicts) that you actually used today, and how. -->
Monday: venv, setting up our environment
Tuesday: Exceptions, raising validationexception
Wednesday: Loggging, logging our sql results



## What we would do differently

<!-- One process improvement for the next pair session, and one thing you need from Friday (joins, GROUP BY, constraints) to make this validation suite better. -->
We would communicate more often instead of silently working and ignorning our partner
We could use group by to count the number of passes and fails
