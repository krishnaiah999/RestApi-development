# main.py

from fastapi import FastAPI, Query
from typing import Optional, List
from students_data import students

app = FastAPI()


@app.get("/students")
def get_students(
    name: Optional[str] = None,
    age: Optional[int] = None,
    grade: Optional[str] = None,
    city: Optional[str] = None
):
    filtered_students = students

    if name:
        filtered_students = [s for s in filtered_students if s["name"].lower() == name.lower()]

    if age:
        filtered_students = [s for s in filtered_students if s["age"] == age]

    if grade:
        filtered_students = [s for s in filtered_students if s["grade"].upper() == grade.upper()]

    if city:
        filtered_students = [s for s in filtered_students if s["city"].lower() == city.lower()]

    return filtered_students

