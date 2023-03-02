from pydantic import BaseModel
from com.data.factory.models.Message import Message


class Request(BaseModel):
    message: Message
