from fastapi import FastAPI
from com.data.factory.models.Request import Request
from com.data.factory.services.InsertService import InsertService

app = FastAPI()


@app.post('/api/v1/insert')
def insert_item(request: Request):
    service = InsertService()
    return service.invoke(request)
