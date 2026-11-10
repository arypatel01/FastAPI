from fastapi import FastAPI
from pydantic import BaseModel, Field , field_validator , model_validator , ConfigDict

app = FastAPI()

class Student(BaseModel):

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment = True
    )

    name: str
    age: int
    city: str

student1 = Student(name="John", age=20, city="New York")



@app.post("/students")
def func(student:Student):
    return {
        "name": student.name,
        "age": student.age,
        "city": student.city
    }


# Pydantic Model Methods

class s2(BaseModel):
    name:str
    age:int
    city:str
    email: str | None = None

stu = s2(name="aryen" , age=19 , city="Unjha" )

dictionary = stu.model_dump()
json = stu.model_dump_json()

data = {
    "name":"aryan",
    "age":19,
    "city":"unjha",
    "email":"aryan@gmail.com"
}

obj = s2.model_validate(data)

excEmail = stu.model_dump(exclude={"email"})

excNone = stu.model_dump(exclude_none=True)

print(dictionary)
print(json)
print(obj)
print(excEmail)
print(excNone)