import unittest
from functions.assert_equal import assert_equal

class TestAssertEqual(unittest.TestCase):
    def test_assert_equal(self):
        actual = assert_equal(5, 6)
        expected = 11
        # check if the actual output of the function and 
        # our expected output are same
        self.assertEqual(expected, actual)