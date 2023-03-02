import unittest
from com.data.factory.adapters.RequestParser import RequestParser
from com.data.factory.utils.logger import logging

LOG = logging.getLogger(__name__)


class testCommon(unittest.TestCase):

    def test_get_method_name_1(self):
        expected = "validMethod"
        request = {
            "protoPayload": {
                "methodName": expected
            }
        }
        parser = RequestParser(request)
        actual = parser.get_method_name()
        self.assertEqual(expected, actual)

    def test_get_method_name_2(self):
        expected = "validMethod"
        request = {"protoPayload": {}}
        parser = RequestParser(request)
        actual = parser.get_method_name()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
