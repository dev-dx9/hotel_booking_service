from typing import Annotated
from fastapi import FastAPI, status, Body, HTTPException
import uvicorn

app = FastAPI()
hotels = [
    {'id': 1, 'title': 'A', 'name': 'A'},
    {'id': 2, 'title': 'B', 'name': 'B'},
]


@app.get('/hotels', status_code=status.HTTP_200_OK)
async def read_hotels() -> list:
    return hotels


@app.put('/hotels/{hotel_id}', status_code=status.HTTP_200_OK)
async def update_hotels(
        hotel_id: int,
        hotel_title: Annotated[str, Body(..., embed=True)],
        hotel_name: Annotated[str, Body(..., embed=True)],
) -> dict:
    hotel = next((h for h in hotels if h['id'] == hotel_id), None)

    if not hotel:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Hotel not found')

    hotel['title'] = hotel_title
    hotel['name'] = hotel_name

    return {'status': 'ok'}


@app.patch('/hotels/{hotel_id}', status_code=status.HTTP_200_OK)
async def update_hotel(
        hotel_id: int,
        hotel_title: Annotated[str, Body(..., embed=True)],
) -> dict:
    hotel = next((h for h in hotels if h['id'] == hotel_id), None)

    if not hotel:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Hotel not found')

    hotel['title'] = hotel_title

    return {'status': 'ok'}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
