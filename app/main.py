from fastapi import FastAPI
from .database import engine, Base
from .models import Department, Job, Employee
from .routers import csv_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(csv_router.router)


@app.get("/")
async def root():

    return {"message": "Globant API success"}
