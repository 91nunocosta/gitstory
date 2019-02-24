from unittest import TestCase

from datetime import datetime

from pygitstory.utils import as_datetime

class TestUtils(TestCase):

    def test_datetime(self):
        datetime_value = datetime(2018, 1, 1, 1, 1, 1)
        self.assertEqual(as_datetime(datetime_value), datetime_value)
        self.assertEqual(as_datetime('2018-01-01 01:01:01'), datetime_value)
        with self.assertRaises(TypeError):
            as_datetime(1)