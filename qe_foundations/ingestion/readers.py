"""qe_foundations/ingestion/readers.py  -  TASK 4 (about 35 min)

One reader per format. Each returns a LIST OF RAW RECORDS and only deals with
FORMAT problems (is this valid CSV / JSON / XML? are the columns there?).
Business rules (is the status allowed? is the duration negative?) belong to
validation.py, NOT here.

Always open files through open_source() from contexts.py.
See README Task 4 for the exact contract of each reader.
"""

import csv
import json
import xml.etree.ElementTree as ET

from .contexts import open_source
from .exceptions import MalformedSourceError, MissingColumnsError
from .validation import REQUIRED_FIELDS


def read_csv_records(path):
    """CSV -> list of raw dicts, one per data row (use csv.DictReader)."""
    HEADERS = ["id","title","status","duration"]
    out = []
    with open_source(path) as file:
        reader = csv.reader(file)
        header = next(reader, [])
        missing = [head for head in HEADERS
                if head not in header]
        if len(missing) > 0:
            raise MissingColumnsError(path, missing)
        file.seek(0)
        data = csv.DictReader(file)

        for row in data:
            out.append(row)
    return out


def read_json_records(path):
    """JSON -> list of raw records. Expected shape: {"suite": ..., "tests": [...]}."""
    with open_source(path) as file:
        try:
            data =  json.load(file)
        except json.JSONDecodeError as e:
            raise MalformedSourceError(path, f"Json is broken at line: {e.lineno} and column: {e.colno}") from e
    if not isinstance(data, dict):
        raise MalformedSourceError(path, "Json does not return dict")
    if data.get("tests", False) == False:
        raise MalformedSourceError(path, "No test in dict")
    if not isinstance(data["tests"], list):
        raise MalformedSourceError(path, "tests is not a list")
    return data["tests"]


def read_xml_records(path):
    """XML -> list of raw dicts, one per <testcase> element at ANY depth."""
    with open_source(path) as file:
        try:
            data = ET.parse(path)
            root =  data.getroot()
        except ET.ParseError as e:
            raise MalformedSourceError(path, f"The source is malformed at {e.position[0]} and {e.position[1]}") from e

    final = []
    for test in root.iter("testcase"):
        out = test.attrib
        title = test.findtext("title", default=None)
        duration = test.findtext("duration", default=None)
        out["title"] = title
        out["duration"] = duration
        if not "id" in out:
            out["id"] = None
        final.append(out)
    return final