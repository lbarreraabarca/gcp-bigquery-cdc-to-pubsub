from pydantic import BaseModel


class PubSub(BaseModel):
    subscription_name: str
    project_id: str
