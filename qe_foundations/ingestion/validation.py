"""qe_foundations/ingestion/validation.py  -  TASK 5 (about 25 min)

validate_record() decides whether ONE raw record is acceptable.

IMPORTANT: this is VALIDATION OF EXTERNAL DATA. Raise exceptions here.
Do NOT use `assert` in this file (assertions can be switched off with `python -O`).
See README Task 5 for the exact rules.
"""

from .exceptions import InvalidValueError, MissingFieldError
import math

REQUIRED_FIELDS = ("id", "title", "status", "duration")
VALID_STATUSES = ("pass", "fail", "blocked")


def validate_record(row, raw):
    """Turn one raw record into a clean dict, or raise a RecordValidationError.

    row : 1-based record number in the file (used in error messages)
    raw : whatever the reader produced for that record (usually a dict)

    Returns {"id": str, "title": str, "status": str, "duration": float}.
    """
    if not isinstance(raw, dict):
        raise InvalidValueError(row, "record", raw, dict)
    
    keys = list(raw.keys())
    miss = [field for field in REQUIRED_FIELDS if field not in raw]
    if miss:
        raise MissingFieldError(row, miss[0])
    for field in REQUIRED_FIELDS:
        if raw[field] == None or str(raw[field]).strip() == "":
            raise MissingFieldError(row, field)

    if not isinstance(raw["status"], str):
        raise InvalidValueError(row, "status", raw["status"], VALID_STATUSES)
    if not raw["status"].strip().lower() in VALID_STATUSES:
        raise InvalidValueError(row, "status", raw["status"], VALID_STATUSES)


    if isinstance(raw["duration"], bool):
        raise InvalidValueError(row, "duration", raw["duration"], float)
    try:
        dur = float(raw["duration"])
    except Exception as e:
        raise InvalidValueError(row, "duration", raw["duration"], float)

    if not math.isfinite(dur) or dur < 0:
        raise InvalidValueError(row, "duration", raw["duration"], float)


    id = str(raw["id"]).strip()

    return {
        "id": id,
        "title": raw["title"].strip(),
        "status": raw["status"].strip().lower(),
        "duration": dur
    }

    
