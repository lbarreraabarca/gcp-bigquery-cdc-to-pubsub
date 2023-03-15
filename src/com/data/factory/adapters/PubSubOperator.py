import json
from google.cloud import pubsub_v1
from com.data.factory.adapters.Base64Encode import Base64Encode
from com.data.factory.models.Request import Request
from com.data.factory.utils.Env import Env
from com.data.factory.utils.logger import logging
from com.data.factory.services.InsertService import InsertService

LOG = logging.getLogger(__name__)


class PubSubOperator():

    def __init__(self, project_id: str) -> None:
        self._project_id = project_id
        self._subscriber = None

    def get_connection(self):
        self._publisher = pubsub_v1.PublisherClient()
        self._subscriber = pubsub_v1.SubscriberClient()

    def publish(self,
                topic_name: str,
                data: str) -> None:
        self.get_connection()
        if topic_name is None or topic_name == "":
            raise Exception("topic_name cannot be None or empty.")
        if data is None or data == "":
            raise Exception("data cannot be None or empty.")
        topic_path = self.publisher.topic_path(self.project_id, topic_name)
        self.publisher.publish(topic_path, data.encode("utf-8"))

    def callback(self, message: pubsub_v1.subscriber.message.Message) -> None:
        message.ack()
        encoder = Base64Encode()
        data = {
            "message": {
                "data": encoder.encode(message.data.decode("utf-8"))
            }
        }
        request = Request(**data)
        service = InsertService()
        service.invoke(request)

    def pull(self,
             subscription_id: str):
        subscription_path = self.subscriber.subscription_path(self.project_id,
                                                              subscription_id)
        streaming_pull_future = self.subscriber \
            .subscribe(subscription_path, callback=self.callback)
        LOG.info(f"Listening for messages on {subscription_path}")
        with self.subscriber:
            try:
                streaming_pull_future.result()
            except Exception as e:
                LOG.error(
                    f"Error from {subscription_path} threw an exception: {e}."
                )
                streaming_pull_future.cancel()
                streaming_pull_future.result()

    @property
    def project_id(self) -> str:
        return self._project_id

    @property
    def publisher(self) -> pubsub_v1.PublisherClient:
        return self._publisher

    @property
    def subscriber(self) -> pubsub_v1.SubscriberClient:
        return self._subscriber
