from fastapi import FastAPI, HTTPException , Path , Query

app = FastAPI()

students_data = {
    "student_1": {
        "name": "Aarav Sharma",
        "roll_no": 101,
        "marks": {
            "maths": 85,
            "phy": 78,
            "chem": 82
        }
    },
    "student_2": {
        "name": "Diya Patel",
        "roll_no": 102,
        "marks": {
            "maths": 92,
            "phy": 88,
            "chem": 91
        }
    },
    "student_3": {
        "name": "Rohan Gupta",
        "roll_no": 103,
        "marks": {
            "maths": 74,
            "phy": 65,
            "chem": 70
        }
    },
    "student_4": {
        "name": "Ananya",
        "roll_no": 104,
        "marks": {
            "maths": 95,
            "phy": 94,
            "chem": 98
        }
    }
}


# Single path parameter
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}


# Multiple path parameters
@app.get("/students/{student_name}/marks/{subject}")
def get_student_marks_by_path(student_name: str, subject: str):

    for i in students_data:
        if students_data.get(i).get("name") == student_name:
            student = i
            break
    else:
        student = -1

    if student == -1:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    marks = students_data.get(student).get("marks")

    if subject not in marks:
        raise HTTPException(
            status_code=404,
            detail="Subject not found"
        )

    return {
        "student_name": student_name,
        "subject": subject,
        "marks": marks.get(subject)
    }


# Multiple query parameters
@app.get("/students/marks")
def get_student_marks_by_query(student_name: str, subject: str):

    for i in students_data:
        if students_data.get(i).get("name") == student_name:
            student = i
            break
    else:
        student = -1

    if student == -1:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    marks = students_data.get(student).get("marks")

    if subject not in marks:
        raise HTTPException(
            status_code=404,
            detail="Subject not found"
        )

    return {
        "student_name": student_name,
        "subject": subject,
        "marks": marks.get(subject)
    }


# Task 2

@app.get("/students/search")
def search_student(
    student_name: str = Query(
        default=...,
        min_length = 3,
        max_length = 30
    )
):
    return{"msg": "Student Found!!!"}

@app.get("/students/{student_id}")
def search_for_student_using_path(
    student_id: int = Path(
        ge=1
    )
):
    return{"msg": "Student Found!!!"}
