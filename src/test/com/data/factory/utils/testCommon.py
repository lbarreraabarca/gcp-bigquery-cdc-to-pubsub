import unittest
from com.data.factory.utils.Common import Common
from com.data.factory.utils.logger import logging

LOG = logging.getLogger(__name__)


class testCommon(unittest.TestCase):

    def test_cast_1(self):
        common = Common()
        expected = "hello world"
        actual = common.cast("'hello world'", "STRING")
        self.assertEqual(expected, actual)

    def test_cast_2(self):
        common = Common()
        expected = 1
        actual = common.cast("1", "INTEGER")
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
