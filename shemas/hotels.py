from pydantic import BaseModel


class HotelBase(BaseModel):
    title: str
    location: str


class HotelCreate(HotelBase):
    pass


class HotelRead(HotelBase):
    id: int


class HotelUpdate(HotelBase):
    pass


class HotelPatch(BaseModel):
    title: str | None
    location: str | None
