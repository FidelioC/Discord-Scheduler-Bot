# test event.py

import unittest
from event import Event


class TestEventUnit(unittest.TestCase):
    def test_date_valid(self):
        print("\nTEST VALID DATE")
        result = Event.verify_date(self, "02-12")
        self.assertTrue(result)
        print("\n")

    def test_date_invalid(self):
        print("\nTEST INVALID DATE\n")
        result = Event.verify_date(self, "100-12")
        self.assertFalse(result)
        print("\n")

    def test_time_valid(self):
        print("\nTEST VALID TIME\n")
        result = Event.verify_time(self, "12:00 pm")
        self.assertTrue(result)

        result = Event.verify_time(self, "1:00 am")
        self.assertTrue(result)
        print("\n")

    def test_time_invalid(self):
        print("\nTEST INVALID TIME\n")
        result = Event.verify_time(self, "100:00 am")
        self.assertFalse(result)

        result = Event.verify_time(self, "10000am")
        self.assertFalse(result)
        print("\n")


if __name__ == "__main__":
    unittest.main()
