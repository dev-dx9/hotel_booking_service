from typing import Annotated
from fastapi import status, Body, HTTPException, APIRouter


router = APIRouter(prefix='/hotels', tags=['hotels'])

hotels = [
    {'id': 1, 'title': 'A', 'name': 'A'},
    {'id': 2, 'title': 'B', 'name': 'B'},
]


@router.get('/', status_code=status.HTTP_200_OK)
async def read_hotels() -> list:
    return hotels


@router.put('/{hotel_id}', status_code=status.HTTP_200_OK)
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


@router.patch('/{hotel_id}', status_code=status.HTTP_200_OK)
async def update_hotel(
        hotel_id: int,
        hotel_title: Annotated[str, Body(..., embed=True)],
) -> dict:
    hotel = next((h for h in hotels if h['id'] == hotel_id), None)

    if not hotel:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Hotel not found')

    hotel['title'] = hotel_title

    return {'status': 'ok'}
