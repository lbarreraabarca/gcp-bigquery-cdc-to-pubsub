import pandas as pd
import re
from com.data.factory.utils.Common import Common


class SQL():

    def create_query(self, job_id: str, region: str = 'region-us') -> str:
        region = "region-us"
        return f"""
            SELECT
                query
            FROM
                {region}.INFORMATION_SCHEMA.JOBS_BY_PROJECT
            WHERE job_id = "{job_id}"
        """

    def get_sql_statement(self, df: pd.DataFrame, job_id: str) -> str:
        if df.size <= 0:
            raise Exception(f"Not found data for job {job_id}")
        statement = str(df["query"][0])
        return statement.strip()

    def get_values_from_insert_statement(self, statement: str) -> list:
        if statement is None or statement == "":
            raise Exception("statement cannot be None or empty.")
        regex = r"([Vv]{1}[Aa]{1}[Ll]{1}[Uu]{1}[Ee]{1}[Ss]{1})"
        statement_splitted = re.split(regex, statement)
        if len(statement_splitted) < 3:
            raise Exception(f"Invalid statement {statement} for {regex}")
        common = Common()
        statement_values = statement_splitted[2].strip()
        values = common.replace_first_occurrence(statement_values,
                                                 "(",
                                                 "")
        values = common.replace_last_occurrence(values, ")", "", 1)
        values = common.replace_last_occurrence(values, ";", "", 1)
        return [value.strip().replace("'", "").replace('"', '')
                for value in values.split(",")]

    def get_json_from_insert_statement(self,
                                       statements: list,
                                       fields: list) -> dict:
        output = {}
        common = Common()
        for i in range(0, len(fields)):
            field_name = fields[i].split(":")[0]
            field_type = fields[i].split(":")[1]
            value = common.cast(statements[i], field_type)
            output[field_name] = value
        return output
