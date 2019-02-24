from datetime import datetime, tzinfo

from dateutil.parser import parse
from dateutil.tz import UTC


def as_datetime(value):
    date = value
    if not isinstance(date, datetime):
        date = parse(value)
    return date.astimezone(UTC)