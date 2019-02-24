from datetime import datetime, timedelta, timezone, tzinfo
from unittest import TestCase

from dateutil.tz import UTC

from pygitstory.utils import as_datetime


class TestUtils(TestCase):

    def test_datetime(self):
        datetime_value = datetime(2018, 1, 1, 3, 1, 1, tzinfo=timezone(timedelta(hours=2)))
        expected_datetime = datetime(2018, 1, 1, 1, 1, 1, tzinfo=UTC)
        self.assertEqual(as_datetime(datetime(2018, 6, 8, 13, 56, 25)), datetime(2018, 6, 8, 13, 56, 25, tzinfo=UTC))
        self.assertEqual(as_datetime(datetime_value), expected_datetime)
        self.assertEqual(as_datetime('2018-01-01T03:01:01+02:00'), expected_datetime)
        self.assertEqual(as_datetime('2018-01-01T01:01:01Z'), datetime(2018, 1, 1, 1, 1, 1, tzinfo=UTC))
        with self.assertRaises(TypeError):
            as_datetime(1)