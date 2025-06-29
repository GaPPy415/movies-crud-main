import time

from fastapi import Depends, FastAPI
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session

from app.crud import create, delete, list_all, read, update
from app.db import SessionLocal, engine
from app.models import Base
from app.schemas import MovieSchema

app = FastAPI()

for i in range(5):
    try:
        Base.metadata.create_all(bind=engine)
        break
    except OperationalError:
        time.sleep(i + 1)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello"}


@app.post("/create")
async def create_movie(schema: MovieSchema, db: Session = Depends(get_db)):
    movie = create(db, schema)

    if movie is None:
        return {"message": "Movie already exists"}
    else:
        return movie


@app.get("/read/{eidr}")
async def read_movie(eidr: str, db: Session = Depends(get_db)):
    movie = read(db, eidr)
    
    if movie is None:
        return {"message": "Movie not found"}
    else:
        return movie


@app.post("/update")
async def update_movie(schema: MovieSchema, db: Session = Depends(get_db)):
    movie = update(db, schema)

    if movie is None:
        return {"message": "Movie not found"}
    else:
        return movie


@app.post("/delete/{eidr}")
async def delete_movie(eidr: str, db: Session = Depends(get_db)):
    movie = delete(db, eidr)

    if movie is None:
        return {"message": "Movie not found"}
    else:
        return movie


@app.get("/list")
async def list_all_movies(db: Session = Depends(get_db)):
    return list_all(db)
