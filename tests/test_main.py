import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Globant API success"}


def test_employees_by_quarter():
    response = client.get("/metrics/employees_by_quarter/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_departments_above_average():
    response = client.get("/metrics/departments_above_average/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
