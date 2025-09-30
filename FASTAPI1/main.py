from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from contextlib import asynccontextmanager
from typing import Annotated
from models import User

DATABASE_URL = "sqlite:///./USER.db"
engine = create_engine(DATABASE_URL, echo=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)

def get_session():
    with Session(engine) as session:
        yield session

sessionDep = Annotated[Session, Depends(get_session)]

# Sample route to test the API
@app.get("/")
def read_root():
    return {"message": "API is working!"}