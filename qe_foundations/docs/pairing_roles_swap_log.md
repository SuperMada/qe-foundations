# Pairing log -- roles and swap schedule

<!--
HOW TO USE: copy this file to  qe_foundations/docs/pairing_log.md.
Fill ONE row at the END of every 30-minute block (it takes one minute). The check
script counts the rows that are filled in; a 3-hour session has 5 driving blocks.
-->

## Roles card (keep it visible)

| | DRIVER | NAVIGATOR |
|---|---|---|
| Hands | the ONLY one on the keyboard | off the keyboard |
| Job | turn the navigator's direction into code; think aloud while typing | read the rule, decide the next step, predict the result, spot typos and edge cases |
| Says things like | "I'm writing the WHERE clause now..." | "Predict first: which run_ids do we expect?" |
| Never | silently type something nobody asked for | grab the mouse or dictate character by character |

**Swap** every 30 minutes, even in the middle of a rule. The outgoing driver commits and pushes
(your own Git name), the new driver runs `git pull`, then types.

## Pair

| | Name | Git user.name (as shown by `git log`) | Machine / repo owner |
|---|---|---|---|
| Partner A | | | |
| Partner B | | | |

Branch: `feature/sql-validation-...`        Remote: ...

## Swap log (one row per block)

| Block | Clock time | Driver | Navigator | Goal of the block | Result (rules done, commit hash) | Predictions: right / wrong |
|---|---|---|---|---|---|---|
| 1 | 1:37-2:01 | Philo Girgis | Adam Fischer | R01-R04 | R01-R04 | 50% right |
| 2 | 2:02-2:14 | Adam Fischer | Philo Girgis | R05-R08 | R05-R08 | 75% right |
| 3 | 2:15-2:45 | Philo Girgis | Adam Fischer | R09-R12 & E01-E02 | R09-R12 & E01-E02 | 50% right |
| 4 | 2:45-3:00::3:20-3:50 | Adam Fischer | Philo Girgis | Python Runner | Logger | N/A |
| 5 | 11:30- | Philo Girgis | Adam Fischer | Python Runner & Unit tests | done  | N/A |

## Disagreements and how we settled them

<!-- At least one honest example: what did you disagree about (query style, a rule's meaning, ...), and how did you decide? -->


## Hints we used

<!-- Which hint levels, for which rules? (Using hints is fine -- hiding it is not.) -->

