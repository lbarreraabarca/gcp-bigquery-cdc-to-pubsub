import json
from com.data.factory.ports.Encoder import Encoder
from com.data.factory.adapters.Base64Encode import Base64Encode
from com.data.factory.adapters.BigQueryOperator import BigQueryOperator
from com.data.factory.adapters.KafkaOperator import KafkaOperator
from com.data.factory.adapters.RequestParser import RequestParser
from com.data.factory.models.Payload import Payload
from com.data.factory.models.Request import Request
from com.data.factory.utils.Env import Env
from com.data.factory.utils.logger import logging
from com.data.factory.utils.SQL import SQL

LOG = logging.getLogger(__name__)


class InsertService(object):
    def invoke(self, request: Request) -> dict:
        try:
            env = Env()
            encoded_data = request.message.data
            LOG.info(f"Processing payload {encoded_data}")
            encoder: Encoder = Base64Encode()
            decoded_data = encoder.decode(encoded_data)
            json_data = json.loads(decoded_data)
            payload = Payload(**json_data)
            parser = RequestParser(payload)
            job_id = parser.get_job_id()
            LOG.info(f"methodName {parser.get_method_name()} JobId {job_id}")

            bq_project_id, bq_dataset_name, bq_table_name = parser \
                .get_resource_specs()

            bigquery_operator = BigQueryOperator()
            sql = SQL()
            query = sql.create_query(job_id=job_id)
            df = bigquery_operator.query(query)
            statement = sql.get_sql_statement(df, job_id)
            statement_list = sql.get_values_from_insert_statement(statement)
            fields_list = bigquery_operator.get_table_schema(bq_project_id,
                                                             bq_dataset_name,
                                                             bq_table_name)
            message = sql.get_json_from_insert_statement(statement_list,
                                                         fields_list)
            LOG.info(message)
            response = {
                "job_id": job_id,
                "message": message
            }
            kafka = KafkaOperator(env.kafka.bootstrap_server,
                                  env.kafka.username,
                                  env.kafka.password)
            kafka.send_data(env.kafka.topic,
                            message)
            LOG.info(f"Data {message} has sent successfully.")
            LOG.info(response)
            return (response, 200)
        except Exception as e:
            return ({
                "response": f"{e}"
                }, 500)
