**Globant Data Engineering Coding Challenge**

This repository contains the solution to a Data Engineering coding challenge. It demonstrates a REST API for data ingestion from CSV files, SQL analytics, Docker containerization, and cloud deployment.

*Project Overview*
The project implements:
    - REST API to upload data from CSV files.
    - Batch insertion of data into an SQL database.
    - SQL endpoints for specific data metrics.
    - Dockerized deployment to a cloud provider.

**Technical Stack & Architecture**

    *Stack:*
    - Language: Python 3.11
    - Web Framework: FastAPI
    - Database: SQLite (simplified for local setup)
    - ORM: SQLAlchemy
    - Testing: pytest
    - Containerization: Docker
    - Deployment Platform: Render.com
    
*Structure:*
    globant-challenge/
    ├── app/
    │ ├── database.py
    │ ├── main.py
    │ ├── models.py
    │ └── routers/
    │ ├── csv_router.py
    │ └── metrics_router.py
    ├── tests/
    │ └── test_main.py
    ├── requirements.txt
    ├── Dockerfile
    └── README.md

**Database Schema**

*Tables:*
    - Employees (employee details)
    - Departments (department details)
    - Jobs (job details)

**REST API**

*CSV Upload:*
    - POST /upload/departments/
    - POST /upload/jobs/
    - POST /upload/employees/

*Metrics:*
    - GET /metrics/employees_by_quarter/ (employees hired per quarter)
    - GET /metrics/departments_above_average/ (departments above average hires)

**Automated Testing**

Tests are implemented using pytest to ensure the correctness of API endpoints.

*Run tests:* 
    pip install pytest
    pytest tests/