import json
from kafka import KafkaProducer


class KafkaOperator():

    def __init__(self,
                 bootstrap_server: str,
                 username: str,
                 password: str):
        self._bootstrap_server = bootstrap_server
        self._username = username
        self._password = password

    def send_data(self, topic: str, data: dict):
        producer = KafkaProducer(bootstrap_servers=self.bootstrap_server,
                                 value_serializer=lambda v:
                                 json.dumps(v).encode('utf-8'),
                                 acks='all',
                                 retries=3,
                                 security_protocol="SASL_SSL",
                                 sasl_mechanism="PLAIN",
                                 sasl_plain_password=self._password,
                                 sasl_plain_username=self._username
                                 )
        try:
            future = producer.send(topic, data)
            self.producer.flush()
            future.get(timeout=60)
            print("message sent successfully...")
            return {'status_code': 200, 'error': None}
        except Exception as ex:
            return ex

    @property
    def bootstrap_server(self) -> str:
        return self._bootstrap_server

    @property
    def username(self) -> str:
        return self._username

    @property
    def password(self) -> str:
        return self._password
