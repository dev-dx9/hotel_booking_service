from fastapi import status, APIRouter, Query
from shemas.hotels import HotelRead

router = APIRouter(prefix='/hotels', tags=['Hotels'])

hotels: list[HotelRead] = [
    HotelRead(id=1, title='A', location='A'),
    HotelRead(id=2, title='B', location='B'),
    HotelRead(id=3, title='C', location='C'),
    HotelRead(id=4, title='D', location='D'),
    HotelRead(id=5, title='E', location='E'),
]


@router.get('/', response_model=list[HotelRead], status_code=status.HTTP_200_OK)
async def read_hotels(
        page: int | None = Query(default=1, ge=1),
        per_page: int | None = Query(default=10, ge=1, le=100)
) -> list[HotelRead]:
    if page is None or per_page is None:
        return hotels

    start = (page - 1) * per_page
    end = start + per_page
    return hotels[start:end]
