from datetime import datetime, tzinfo

from dateutil.parser import parse
from dateutil.tz import UTC


def as_datetime(value):
    date = value
    if not isinstance(date, datetime):
        date = parse(value)
    if date.tzinfo is not None:
        date = date.astimezone(UTC)
    else:
        date = date.replace(tzinfo=UTC)
    return date
