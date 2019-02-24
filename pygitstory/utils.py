from datetime import datetime

from dateutil.parser import parse

def as_datetime(value):
    if isinstance(value, datetime):
        return value
    else:
        return parse(value)
