from fastapi import FastAPI
from .routers import memes
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(memes.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}