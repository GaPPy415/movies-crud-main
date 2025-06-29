from pydantic import BaseModel


class MovieSchema(BaseModel):
    eidr: str
    title: str
    director: str
    year: int
    genre: str
    price: float
    rating: float
