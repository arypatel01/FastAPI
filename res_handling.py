from fastapi import FastAPI , HTTPException, Response
from pydantic import BaseModel
import json

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



# Practice task

# Requirements:
# 1. Accept sid from the URL.
# 2. Check whether the student exists.
# 3. If the student doesn't exist, raise HTTPException with status 404.
# 4. If the student exists, return the student's name and city as a normal dictionary.
# 5. Use the injected Response parameter to set:
#    - Status code: 200
#    - Header: X-Student-Status
#    - Value: Found

@app.get("/student/{sid}" , response_model=StudentResponse)
def chekc_student(sid: int):
    if sid not in student_db:
        raise HTTPException(
            status_code = 404,
            detail = "Student not Found!!!"
        )
    student_data = {
        "name": student_db[sid]["name"],
        "city": student_db[sid]["city"]
    }
    return Response(
        content = json.dumps(student_data),
        status_code = 200,
        headers = {"X-Student-Status": "Found"},
        media_type="application/json"
        # value = "Found"
    )

# cookie handling 

@app.get("/setcookie")
def setCookie(response: Response):
    response.set_cookie(
        key="name",
        value="Aryan"
    )

@app.get("/deletecookie")
def deleteCookie(response: Response):
    response.delete_cookie(
        key="name"
    )
