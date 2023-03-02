from pydantic import BaseModel
from com.data.factory.models.ProtoPayload import ProtoPayload


class Payload(BaseModel):
    protoPayload: ProtoPayload
