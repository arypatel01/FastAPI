from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

student_db = {
    101: {
        "name": "Aryan",
        "age": 19,
        "city": "Ahmedabad",
        "course": "BTech",
        "password": "aryan123"
    },
    102: {
        "name": "Rahul",
        "age": 20,
        "city": "Surat",
        "course": "BCA",
        "password": "rahul123"
    },
    103: {
        "name": "Meet",
        "age": 19,
        "city": "Vadodara",
        "course": "BTech",
        "password": "meet123"
    }
}

class Student(BaseModel):
    name: str
    age: int
    city: str
    course: str
    password: str

class StudentResponse(BaseModel):
    name: str
    age: int
    city: str
    course: str


@app.get("/student",response_model=StudentResponse)
def students(student: Student):
    return student


@app.post("/student",response_model=StudentResponse)
def student_res(student: Student):
    dict_student = student.model_dump()
    student_db[len(student_db)+101] = dict_student
    return student


