# 8. Your coding assignment
# Create a small Student API with these requirements:
# 1. GET /students → Return all students.
# 2. GET /students/{student_id} → Return one student.
# 3. If the student ID is not 1, raise a 404 error.
# 4. Use a Student Pydantic model as the response model.
# 5. Add tags and summary to your GET endpoints.
# 6. POST /students → Return a 201 status code.


from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    name: str
    age: int
    city: str


@app.get("/students" ,
         summary="it is giving the student data" ,
         tags=["Student"]
        )
def get_student():
    return {"student1":1}



@app.get("/students/{student_id}" ,
          response_model= Student ,
          summary="It is giving the data for specified student" ,
          tags=["Student"] 
        )
def student(student_id: int):
    if student_id != 1:
        raise HTTPException(
            status_code=404,
            detail="student not found"
        )
    return {
        "name":"name",
        "age":12,
        "city":"Ahmedabad"
    }

@app.post("/studentData" , status_code=201)
def function():
    return {"student":1}

