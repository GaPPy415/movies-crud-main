import os

from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

POSTGRES_URL = os.getenv("POSTGRES_URL")
POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", 5432)

if POSTGRES_URL is None:
    raise RuntimeError("Environment variable POSTGRES_URL is not set")

if POSTGRES_DATABASE is None:
    raise RuntimeError("Environment variable POSTGRES_DATABASE is not set")

if POSTGRES_USER is None:
    raise RuntimeError("Environment variable POSTGRES_USER is not set")

url = URL.create(
    drivername="postgresql",
    username=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_URL,
    database=POSTGRES_DATABASE,
    port=POSTGRES_PORT
)
engine = create_engine(url)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
