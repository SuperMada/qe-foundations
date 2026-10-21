"""qe_foundations/ingestion/loader.py  -  TASK 6 (about 30 min)

Ties everything together:
    file -> reader (format) -> validate_record (rules) -> IngestionReport

Error POLICY (the heart of the milestone):
    SourceError            -> the whole file is unusable -> let it propagate (raise)
    RecordValidationError  -> one record is bad          -> COLLECT it and carry on

Already done for you: the IngestionReport and BatchResult classes' constructors
and the READERS lookup table. You write the TODOs.
"""

import csv
from pathlib import Path

from .contexts import LoadSession
from .exceptions import (
    DuplicateIdError,
    RecordValidationError,
    SourceError,
    SourceNotFoundError,
    UnsupportedFormatError,
)
from .readers import read_csv_records, read_json_records, read_xml_records
from .validation import validate_record

# Which reader handles which file extension (always compare lower-case suffixes).
READERS = {
    ".csv": read_csv_records,
    ".json": read_json_records,
    ".xml": read_xml_records,
}


class IngestionReport:
    """Result of loading ONE file: the valid records AND every rejected one."""

    def __init__(self, source, rows_seen=0):
        self.source = source
        self.rows_seen = rows_seen
        self.valid = []       # clean dicts returned by validate_record
        self.rejected = []    # RecordValidationError instances

    def summary(self):
        """TODO (6A): one line, EXACTLY this shape:

            test_cases_messy.csv: 10 rows seen, 3 valid, 7 rejected
        """
        return f"{self.source}: {self.rows_seen} rows seen, {len(self.valid)} valid, {len(self.rejected)} rejected" 

    def rejected_rows(self):
        """TODO (6A): the rejected records as plain dicts, ordered by row number.

        Each dict has exactly the keys: "source", "row", "field", "reason"
        ("reason" is the text of the exception, str(error)).
        """
        rows = [
            {"source": self.source, "row": e.row, "field": e.field, "reason": str(e)}
            for e in self.rejected
        ]
        return sorted(rows, key=lambda r: r["row"])

    def check_invariants(self):
        """TODO (6B): use `assert` statements to check OUR OWN bookkeeping.

        Three invariants (README Task 6B). Each assert gets a helpful message.
        A failure here would be a BUG in this module, not bad input data.
        """
        assert len(self.valid)+len(self.rejected)==self.rows_seen, "The length of valid and rejected is not the length of rows seen"
        seen = set()
        for row in self.valid:
            assert not row['id'] in seen, "Duplicate ids exists"
            seen.add(row['id'])
        for error in self.rejected:
            assert isinstance(error, RecordValidationError), "Rejcted includes non Record Validation Errors"
        return self


class BatchResult:
    """Result of loading a whole folder."""

    def __init__(self):
        self.reports = []           # IngestionReport, one per file that could be read
        self.failed_sources = []    # SourceError instances, one per unusable file

    def totals(self):
        """TODO (6D): return a dict with exactly these keys:

            "files_ok", "files_failed", "valid", "rejected"
        """
        valid = 0
        rejected = 0
        for report in self.reports:
            valid += len(report.valid) 
            rejected += len(report.rejected)

        return {"files_ok": len(self.reports), "files_failed": len(self.failed_sources), "valid": valid, "rejected": rejected}


def load_test_cases(path):
    """Load one CSV/JSON/XML file into an IngestionReport (TODO 6C).

    * Wrap the whole job in `with LoadSession(path):`
    * unknown extension -> raise UnsupportedFormatError
    * SourceError subclasses from the readers must propagate unchanged
    * rows are numbered from 1 (the header line of a CSV does not count)
    * bad records are COLLECTED in report.rejected, good ones go to report.valid
    * a repeated id -> DuplicateIdError for the LATER occurrence (the first one stays valid)
    * call report.check_invariants() before returning
    """
    with LoadSession(path):
        if isinstance(path, str):
            suf = '.'
            name, _ = path.split('.')
            suf += _
        else:
            suf = path.suffix
            name = path.name
        if suf.lower() in READERS:
            reader = READERS[suf.lower()]
        else:
            raise UnsupportedFormatError(path, suf)

        try:
            data = reader(path)
        except SourceError as e:
            raise e

        row = 1
        rejected = []
        valid = []
        for d in data:
            try:
                val = validate_record(row, d)
                for v in valid:
                    if val["id"] in v["id"]:
                        raise DuplicateIdError(row, val["id"])
                row += 1
                valid.append(val)
            except RecordValidationError as e:
                rejected.append(e)
                row+=1
        #Becuase row starts at 1 we -1
        report = IngestionReport(name, row-1)
        report.valid = valid
        report.rejected = rejected
        return report.check_invariants()





def load_directory(folder):
    """Load every file directly inside `folder` (TODO 6D).

    * sorted by file name; sub-folders are skipped
    * a bad FILE never stops the batch: collect its SourceError in failed_sources
    * a folder that does not exist (or is not a folder) -> raise SourceNotFoundError(folder)
    """
    try:
        files = [f for f in folder.iterdir() if f.is_file()]
    except FileNotFoundError as e:
        raise SourceNotFoundError(folder)
    sources = []
    failed_sources = []
    for file in files:
        try:
            sources.append(load_test_cases(file))
        except SourceError as e:
            failed_sources.append(e)
        except Exception as e:
            raise e
    
    sources = sorted(sources, key=lambda r: r.source)
    batch = BatchResult()
    for source in sources:
        batch.reports.append(source)
    for source in failed_sources:
        batch.failed_sources.append(source)

    return batch


def write_rejected_csv(report, out_path):
    """Write report.rejected_rows() to a CSV file (TODO 6E) and return the Path.

    Header exactly: source,row,field,reason     (use csv.DictWriter)
    Create the parent folder if needed. Open the file with newline="".
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["source", "row", "field", "reason"])
        writer.writeheader()
        writer.writerows(report.rejected_rows())
    return out_path