#isAww
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hi": "World"}

@app.get("/dataWP/{data_id}")
async def get_data(data_id: int):
    return {"data": f"{data_id}"}

@app.get("/data/")
async def  data(data_id):
    return {"data": f"{data_id}"}