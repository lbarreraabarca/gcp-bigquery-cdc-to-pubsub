from pydantic import BaseModel
from com.data.factory.models.TableDataChange import TableDataChange


class Metadata(BaseModel):
    tableDataChange: TableDataChange
