from fastapi import FastAPI
from src.service import get_random_berry, calculate_some_value


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/calc")
async def get_calc(x: int = 0):
    return {"result": await calculate_some_value(x)}


@app.get("/berry")
async def get_berry():
    return {"berry": await get_random_berry()}
