from google.cloud import bigquery
import pandas as pd


class BigQueryOperator():

    def __init__(self) -> None:
        self._client = bigquery.Client()

    def query(self, query: str) -> pd.DataFrame:
        if query is None or query == "":
            raise ValueError("query cannot be None or empty.")
        job = self.client.query(query)
        return job.to_dataframe()

    def get_table_schema(self,
                         project_id: str,
                         dataset_name: str,
                         table_name: str) -> list:
        table_id = f"{project_id}.{dataset_name}.{table_name}"
        table_spec = self.client.get_table(table_id)
        return ["{0}:{1}".format(schema.name, schema.field_type)
                for schema in table_spec.schema]

    @property
    def client(self):
        return self._client
