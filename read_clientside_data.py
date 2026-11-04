from fastapi import FastAPI, HTTPException, status , Body
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    city: str


@app.post("/student")
def get_student(
    name: str = Body(),
    age: int = Body(),
    city: str = Body()
):
    return {
    "message": "Student created successfully",
    "student_data": {"name":name , "age": age , "city": city}
}