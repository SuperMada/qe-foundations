# SELECTION_LOG.md (Task 7)

Fill in the "Selected" column by running the command with `--collect-only -q` and counting
test lines, or by reading the summary line. Then write one sentence on when you would use it.

| Command | Selected | When would a team run this? |
|---|---|---|
| `python -m pytest -m smoke` | 7 | To make sure the main functions of the code works |
| `python -m pytest -m "regression and not slow"` | 11 | To test old code still works while avoiding slow tests |
| `python -m pytest -m boundary` | 10 | To test the boundary handling of the code |
| `python -m pytest -k username` | 7 | To test the username functions |
| `python -m pytest -k "grade and not raises"` | 4 | To check the grade tests without and of the exception throwing |
| `python -m pytest tests/test_cart.py::TestCartTotal::test_empty_cart_total_is_zero` | 1 | To run that specific test |

## Questions
1. Temporarily change one `@pytest.mark.smoke` to `@pytest.mark.smok` (typo) and run pytest. What happens and what exit code do you get? Why is that useful? (Undo the typo afterwards!)
   The tests end with an error on the typo, the error message points us directly to the file the marker error was found. This is useful because you mark tests so that they run under that marker and if one of them does not run our system may not be ready
2. What exit code did a run that selected zero tests give? (Try `-k zzzz`.) The exit code was 0 meaning the code executed with zero errors, this because the flag just told the code only to select the specific flag and that flag did not exist so all thests were deselected but the code still ran fine.
3. Which test is your xfail, and what would you see if the bug were fixed (strict=True)? The test would fail if the test was rerun because it is expected the test will fail and because it didnt we would get a red error instead of a yellow warning

## Reading a failure
The output given when a failure occurs shows us what the test was and the code that ran inside of the test. It shows us where the test is and the file it ran in