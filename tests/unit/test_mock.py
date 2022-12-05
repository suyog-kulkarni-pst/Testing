import unittest
import mock

from functions.mock import rand_int


class TestMock(unittest.TestCase):
    @mock.patch("functions.mock.random.randint", return_value=5)
    def test_mock(self, _):
        actual = rand_int()
        expected = 5
        self.assertEqual(expected, actual)




