# test_main.py

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_all_students():
    response = client.get("/students")
    assert response.status_code == 200
    assert len(response.json()) == 10

def test_filter_by_city():
    response = client.get("/students?city=Hyderabad")
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_filter_by_grade():
    response = client.get("/students?grade=A")
    assert response.status_code == 200
    assert all(student["grade"] == "A" for student in response.json())

def test_no_match():
    response = client.get("/students?name=Unknown")
    assert response.status_code == 200
    assert response.json() == []
