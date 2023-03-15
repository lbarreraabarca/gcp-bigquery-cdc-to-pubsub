from pydantic import BaseModel


class Kafka(BaseModel):
    username: str
    password: str
    bootstrap_server: str
    topic: str
