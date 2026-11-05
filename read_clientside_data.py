from fastapi import FastAPI, HTTPException, status , Body , Header , Cookie , Path , Query
from typing import Annotated, Optional
from pydantic import BaseModel

app = FastAPI()

# 7. Module 4 — Final practice

@app.post("/students/{student_id}/marks")
def get_marks(
    student_id: Annotated[int,Path(gt=0)],
    subject: Annotated[str , Query(min_length=2)],
    marks: Annotated[int , Body(ge=0 , le=100)],
    user_agent: Annotated[str | None , Header()] = None
):
    return {
        "student_id":student_id,
        "subject":subject,
        "marks":marks,
        "user_agents":user_agent
    }