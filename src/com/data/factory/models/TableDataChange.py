from pydantic import BaseModel


class TableDataChange(BaseModel):
    jobName: str
