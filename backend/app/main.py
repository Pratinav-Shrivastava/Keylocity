from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base

from app.models import user, score


app = FastAPI(title="Keylocity API")

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Welcome to Keylocity"}