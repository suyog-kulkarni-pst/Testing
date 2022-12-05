from logging import warning
from unittest import TestCase
import unittest
from functions.assert_logs import assert_logs

class TestMain(unittest.TestCase):
    def test_assert_logs(self):
        # with self.assertLogs(logger ,"WARNING / INFO etc.") as log:
        with self.assertLogs("assert_logs.py" ,level="WARNING") as log:
            assert_logs()
            self.assertEqual(log.output, ['WARNING:assert_logs.py:warning from main.py'])
