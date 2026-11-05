from fastapi import FastAPI, HTTPException, status , Body , Header , Cookie
from pydantic import BaseModel

app = FastAPI()

# Task 1 Nested model

class Marks(BaseModel):
    maths: int
    phy: int
    chem: int

class Student(BaseModel):
    name: str
    age: int
    grade: str
    email: str | None = None #Task 2 — Optional field
    marks: Marks

@app.get("/device")
def device(user_agent: str = Header()): #Task 3 — Header
    return {"User-Agent": user_agent}

@app.get("/session")
def session(session_id: int | None = Cookie(default = None)):
    return {"session_id": session_id}