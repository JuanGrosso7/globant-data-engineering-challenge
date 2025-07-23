from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from ..database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Number of employees hired for each job and department in 2021 divided by quarter. The table must be ordered alphabetically by department and job.

@router.get("/metrics/employees_by_quarter/")
async def employees_by_quarter(db: Session = Depends(get_db)):
    query = text("""
        SELECT
            d.department,
            j.job,
            SUM(CASE WHEN strftime('%m', e.datetime) IN ('01','02','03') THEN 1 ELSE 0 END) AS Q1,
            SUM(CASE WHEN strftime('%m', e.datetime) IN ('04','05','06') THEN 1 ELSE 0 END) AS Q2,
            SUM(CASE WHEN strftime('%m', e.datetime) IN ('07','08','09') THEN 1 ELSE 0 END) AS Q3,
            SUM(CASE WHEN strftime('%m', e.datetime) IN ('10','11','12') THEN 1 ELSE 0 END) AS Q4
        FROM employees e
        JOIN departments d ON e.department_id = d.id
        JOIN jobs j ON e.job_id = j.id
        WHERE strftime('%Y', e.datetime) = '2021'
        GROUP BY d.department, j.job
        ORDER BY d.department ASC, j.job ASC;
    """)
    result = db.execute(query).mappings().all()
    return result

# List of ids, name and number of employees hired of each department that hired more employees than the mean of employees hired in 2021 for all the departments, ordered by the number of employees hired (descending).

@router.get("/metrics/departments_above_average/")
async def departments_above_average(db: Session = Depends(get_db)):
    query = text("""
        WITH hires_per_department AS (
            SELECT 
                d.id, d.department, COUNT(e.id) AS hired
            FROM employees e
            JOIN departments d ON e.department_id = d.id
            WHERE strftime('%Y', e.datetime) = '2021'
            GROUP BY d.id, d.department
        )
        SELECT id, department, hired
        FROM hires_per_department
        WHERE hired > (SELECT AVG(hired) FROM hires_per_department)
        ORDER BY hired DESC;
    """)
    result = db.execute(query).mappings().all()
    return result
