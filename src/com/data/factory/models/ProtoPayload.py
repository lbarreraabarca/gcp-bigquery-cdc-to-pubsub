from pydantic import BaseModel
from com.data.factory.models.Metadata import Metadata


class ProtoPayload(BaseModel):
    methodName: str
    resourceName: str
    metadata: Metadata
