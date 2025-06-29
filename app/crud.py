from sqlalchemy.orm import Session
from . import models
from . import schemas


def create(db: Session, schema: schemas.MovieSchema):
    """
    Create a movie.

    Args:
        db (Session): The database session object.
        schema (MovieSchema): The movie schema.

    Returns:
        Movie | None: The created movie, unless one with the same EIDR already exists.
    """
    
    existing_movie = read(db, schema.eidr)

    if existing_movie is not None:
        return None

    movie = models.Movie(
        eidr=schema.eidr,
        title=schema.title,
        director=schema.director,
        year=schema.year,
        genre=schema.genre,
        price=schema.price,
        rating=schema.rating,
    )
    db.add(movie)
    db.commit()
    db.refresh(movie)

    return movie


def read(db: Session, eidr: str):
    """
    Read a movie.

    Args:
        db (Session): The database session object.
        eidr (str): The EIDR of the movie.

    Returns:
        Movie | None: The movie, if it exists.
    """

    return db.query(models.Movie).filter(models.Movie.eidr == eidr).first()


def update(db: Session, schema: schemas.MovieSchema):
    """
    Update a movie.

    Args:
        db (Session): The database session object.
        schema (MovieSchema): The book schema.

    Returns:
        Movie | None: The movie, if it exists.
    """

    movie = read(db, schema.eidr)

    if movie is None:
        return None

    movie.title = schema.title
    movie.director = schema.director
    movie.year = schema.year
    movie.genre = schema.genre
    movie.price = schema.price
    movie.rating = schema.rating

    db.commit()
    db.refresh(movie)

    return movie


def delete(db: Session, eidr: str):
    """
    Delete a movie.

    Args:
        db (Session): The database session object.
        EIDR (str): The EIDR of the movie.

    Returns:
        Movie | None: The movie, if it exists.
    """

    movie = read(db, eidr)

    if movie is None:
        return None

    db.delete(movie)
    db.commit()

    return movie


def list_all(db: Session):
    """
    Get all movies.

    Args:
        db (Session): The database session object.

    Returns:
        list[Movie]: The list of all movies.
    """

    return db.query(models.Movie).all()
