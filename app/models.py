from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    ...


class Movie(Base):
    __tablename__ = "movies"

    eidr: Mapped[str] = mapped_column(primary_key=True)
    title: Mapped[str]
    director: Mapped[str]
    year: Mapped[int]
    genre: Mapped[str]
    price: Mapped[float]
    rating: Mapped[float]

    def __repr__(self) -> str:
        return f"{self.title!r} ({self.eidr!r})"
