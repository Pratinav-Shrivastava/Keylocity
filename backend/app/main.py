from fastapi import FastAPI

from app.db.session import engine
from app.db.base import Base

from app.models.user import User
from app.models.score import Score

from app.api.auth import router as auth_router


app = FastAPI(title="Keylocity API")


# print("Tables registered in metadata:", Base.metadata.tables.keys())

Base.metadata.create_all(bind=engine)


app.include_router(auth_router)


@app.get("/")
def root():
    return {"message": "Welcome to Keylocity"}