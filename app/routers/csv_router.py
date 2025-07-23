from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
import pandas as pd
from io import StringIO
from ..database import SessionLocal
from ..models import Department, Job, Employee

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload/departments/")
async def upload_departments(file: UploadFile = File(...), db: Session = Depends(get_db)):
    content = await file.read()
    df = pd.read_csv(StringIO(content.decode("utf-8")), names=["id", "department"], header=0)


    data = df.to_dict(orient="records")
    for item in data:
        department = Department(**item)
        db.add(department)
    db.commit()

    return {"status": "departments uploaded successfully"}

@router.post("/upload/jobs/")
async def upload_jobs(file: UploadFile = File(...), db: Session = Depends(get_db)):
    content = await file.read()
    df = pd.read_csv(StringIO(content.decode("utf-8")), names=["id", "job"], header=0)


    data = df.to_dict(orient="records")
    for item in data:
        job = Job(**item)
        db.add(job)
    db.commit()

    return {"status": "jobs uploaded successfully"}

@router.post("/upload/employees/")
async def upload_employees(file: UploadFile = File(...), db: Session = Depends(get_db)):
    content = await file.read()
    df = pd.read_csv(StringIO(content.decode("utf-8")), 
                     names=["id", "name", "datetime", "department_id", "job_id"], 
                     header=0)

    df["datetime"] = pd.to_datetime(df["datetime"], errors='coerce')

    df.dropna(subset=["id", "name", "datetime", "department_id", "job_id"], inplace=True)

    df["id"] = df["id"].astype(int)
    df["department_id"] = df["department_id"].astype(int)
    df["job_id"] = df["job_id"].astype(int)

    data = df.to_dict(orient="records")

    for item in data:
        employee = Employee(**item)
        db.add(employee)
        
    db.commit()

    return {"status": "employees uploaded successfully"}
