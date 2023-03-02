import os


class EnvironmentVariables():

    def __init__(self) -> None:
        self._kafka_config = None

    def get_env_vars(self) -> None:
        self.kafka_config = os.getenv("KAFKA_CONFIG")

    @property
    def kafka_config(self) -> str:
        return self._kafka_config

    @kafka_config.setter
    def kafka_config(self, value: str) -> None:
        self._kafka_config = value
