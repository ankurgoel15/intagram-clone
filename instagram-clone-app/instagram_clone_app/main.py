from fastapi import FastAPI
from db import models
from db.database import engine
from routers import api

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(api.api_router)

@app.get("/")
def hello():
    return {"message": "Hello World"}