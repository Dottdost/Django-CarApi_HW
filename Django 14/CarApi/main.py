from http.client import HTTPException
from fastapi import FastAPI
from typing import List, Optional
from models import CarRead, CarCreate
from In_memory_data import _store
from car_repository_service import _create_car, _get_car_by_id, _delete_car

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post('/cars', response_model=CarRead, status_code=201)
def create_car(payload: CarCreate):
    return _create_car(payload)

@app.get('/cars', response_model=List[CarRead])
def get_all_cars(model: Optional[str] = None,
    manufacturer: Optional[str] = None,
    limit: int = 100,
    offset: int = 0):
    items =list(_store.values())

    if model:
        items = [c for c in items if model.lower() in c.model.lower()]
    if manufacturer:
        items = [c for c in items if manufacturer.lower() in c.manufacturer.lower()]
    offset = offset * limit
    return items[offset : offset + limit]

@app.get('/cars/{car_id}', response_model=CarRead)
def get_car_by_id(car_id: int):
    return _get_car_by_id(car_id)

@app.delete('/cars/{car_id}', status_code=204)
def delete_car(car_id: int):
    _delete_car(car_id)
    return None