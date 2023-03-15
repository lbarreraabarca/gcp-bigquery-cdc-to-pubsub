import os
from com.data.factory.models.Kafka import Kafka
from com.data.factory.models.PubSub import PubSub


class Env():

    def __init__(self) -> None:
        self._kafka: Kafka = Kafka(**self.get_kafka_var())
        self._pub_sub: PubSub = PubSub(**self.get_pub_sub_var())

    def get_kafka_var(self) -> dict:
        return {
            "username": os.getenv("KAFKA_USERNAME"),
            "password": os.getenv("KAFKA_PASSWORD"),
            "bootstrap_server": os.getenv("KAFKA_BOOTSTRAP_SERVER"),
            "topic": os.getenv("KAFKA_TOPIC_NAME")
        }

    def get_pub_sub_var(self) -> dict:
        return {
            "project_id": os.environ.get("GCP_PROJECT_ID"),
            "subscription_name": os.environ.get("PUBSUB_SUBSCRIPTION_NAME")
        }

    @property
    def kafka(self) -> Kafka:
        return self._kafka

    @property
    def pub_sub(self) -> PubSub:
        return self._pub_sub
