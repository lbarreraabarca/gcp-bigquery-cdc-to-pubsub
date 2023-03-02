import base64
from com.data.factory.ports.Encoder import Encoder


class Base64Encode(Encoder):

    def encode(self, text: str) -> str:
        if text is None or text == "":
            raise ValueError("text cannot be None or empty.")
        text_bytes = text.encode("utf-8")
        return base64.b64encode(text_bytes).decode("utf-8")

    def decode(self, text: str) -> str:
        if text is None or text == "":
            raise ValueError("text cannot be None or empty.")
        text_bytes = text.encode("utf-8")
        return base64.b64decode(text_bytes).decode("utf-8")
