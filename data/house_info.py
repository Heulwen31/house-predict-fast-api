from pydantic import BaseModel


class HouseInfo(BaseModel):
    district: str = None
    ward: str = None
    house_type: str = None
    legal_type: str = None
    number_floor: float = None
    number_room: int = None
    area: float = None
    width: float = None
    length: float = None
