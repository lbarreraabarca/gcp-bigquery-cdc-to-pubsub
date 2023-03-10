import unittest
from com.data.factory.utils.SQL import SQL
from com.data.factory.utils.logger import logging

LOG = logging.getLogger(__name__)


class test_SQL(unittest.TestCase):

    def test_get_values_from_insert_statement_1(self):
        sql = SQL()
        statement = "INSERT INTO table values ('my message', 2)"
        expected = ["my message", "2"]
        actual = sql.get_values_from_insert_statement(statement)
        self.assertEqual(expected, actual)

    def test_get_values_from_insert_statement_2(self):
        sql = SQL()
        statement = "INSERT INTO table Values (1, 'second ')"
        expected = ["1", "second "]
        actual = sql.get_values_from_insert_statement(statement)
        self.assertEqual(expected, actual)

    def test_get_values_from_insert_statement_3(self):
        sql = SQL()
        with self.assertRaises(Exception) as e:
            sql.get_values_from_insert_statement(None)

    def test_get_values_from_insert_statement_3(self):
        sql = SQL()
        with self.assertRaises(Exception) as e:
            sql.get_values_from_insert_statement("")

    def test_get_values_from_insert_statement_4(self):
        sql = SQL()
        with self.assertRaises(Exception) as e:
            sql.get_values_from_insert_statement("no sql statement")

    def test_get_values_from_insert_statement_5(self):
        sql = SQL()
        statement = "INSERT INTO table values('my message', 2)"
        expected = ["my message", "2"]
        actual = sql.get_values_from_insert_statement(statement)
        self.assertEqual(expected, actual)

    def test_get_values_from_insert_statement_6(self):
        sql = SQL()
        statement = "INSERT INTO table(field1, field2) values('my message', 2)"
        expected = ["my message", "2"]
        actual = sql.get_values_from_insert_statement(statement)
        self.assertEqual(expected, actual)

    def test_get_values_from_insert_statement_7(self):
        sql = SQL()
        statement = "INSERT INTO table (field1, field2) values('my', 0.7)"
        expected = ["my", "0.7"]
        actual = sql.get_values_from_insert_statement(statement)
        self.assertEqual(expected, actual)

    def test_create_query_1(self):
        sql = SQL()
        job_id = "1"
        actual = sql.create_query(job_id)
        self.assertTrue("1" in actual)

    def test_get_json_from_insert_statement_1(self):
        sql = SQL()
        statements = ["1", "text", "2023-02-23 12:07:24.246459 UTC"]
        fields = ["f1:INTEGER", "f2:STRING", "f3:TIMESTAMP"]
        expected = {
            "f1": 1,
            "f2": "text",
            "f3": "2023-02-23 12:07:24.246459 UTC"
        }
        actual = sql.get_json_from_insert_statement(statements, fields)
        self.assertEqual(expected, actual)

    def test_get_json_from_insert_statement_2(self):
        sql = SQL()
        statements = ["1", "text", "2023-02-23 12:07:24.246459 UTC"]
        fields = ["f1:INTEGER", "f2:STRING"]
        with self.assertRaises(Exception) as e:
            sql.get_json_from_insert_statement(statements, fields)


if __name__ == '__main__':
    unittest.main()
