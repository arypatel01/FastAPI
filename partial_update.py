from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

student_db = {
    101: {
        "name": "Aryan",
        "age": 19,
        "city": "Ahmedabad",
        "course": "BTech"
    },
    102: {
        "name": "Rahul",
        "age": 20,
        "city": "Surat",
        "course": "BCA"
    },
    103: {
        "name": "Meet",
        "age": 19,
        "city": "Vadodara",
        "course": "BTech"
    }
}


class StudentUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    city: str | None = None
    course: str | None = None

@app.patch("/students/{student_id}")
def update_student(student_id: int, student: StudentUpdate):

    if student_id not in student_db:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    update_data = student.model_dump(exclude_unset=True)

    student_db[student_id].update(update_data)

    return {
        "message": "Student updated successfully",
        "student": student_db[student_id]
    }


@app.delete("/student/delete/{sid}")
def delete_student(sid:int):
    if sid not in student_db:
        raise HTTPException(
            status_code=404,
            detail="student not found!!!"
        )

    removed = student_db.pop(sid)
    
    return {
        "dict":student_db,
        "msg":"student deleted successfully"
    }
