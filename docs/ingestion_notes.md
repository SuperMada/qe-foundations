# Ingestion module - design notes (Week 2, Day 2)

Answer in your own words, 2-4 sentences each. Replace every line that starts with
. (Delete nothing else.)

## 1. Exceptions or assertions?
In `validate_record` I raise exceptions for a negative duration, but in
`IngestionReport.check_invariants` I use `assert`. Why is each the right tool there?

We use the assert instead of raising exceptions while checking invariants becuase the information in the reports are logically correct but need to be checked one last time before being designated as good where negative durations do not make logical sense.

## 2. Stop or collect?
Why is a malformed JSON file a `SourceError` that stops loading, while a record with
a bad status is a `RecordValidationError` that is collected? Who benefits from this split?

A malformed JSON file is a source error whereas a bad status is a Record Validaton Error because a malformed JSON file will be difficult to impossible for our code to read properly, a bad status can be avoided while still reading in the other data from the file.

## 3. What did the context managers buy you?
Name two things that `open_source` / `LoadSession` do for the caller that you would otherwise
have to remember to do at every call site.

Two things that open_source and LoadSession did for the caller that otherwise would have had to be done manually are open and close the file pointer, making sure to do it when exceptions were raised as well. The second thing that LoadSession did for the caller was track time between the open and close of the session. 

## 4. Your hardest bad-input case
Which sample file or record took you longest to handle, and what was the cause?

The records that took the lognest for me to handle were the ones that had stange durations like nan and inf as I had never dealt with float("nan) and float("inf") before and was not sure with their behaviour or if they could even be cast to floats without error