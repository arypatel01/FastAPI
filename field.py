# Basically feild is used to apply all the conditions on the user input to the directly BaseModel instead of Doing those Path , Query or else

from fastapi import FastAPI
from pydantic import BaseModel, Field , field_validator , model_validator

app = FastAPI()

class Student(BaseModel):
    name: str = Field(
        min_length=3,
        max_length=30
    )

    age: int = Field(
        ge=18,
        le=60
    )

    email: str | None = None

    maths: int = Field(
        ge=0,
        le=100
    )

    physics: int = Field(
        ge=0,
        le=100
    )

    chemistry: int = Field(
        ge=0,
        le=100
    )


@app.post("/students")
def create_student(student: Student):
    return {
        "message": "Student registered successfully",
        "student": student
    }


# Task 

# class Product(BaseModel):
#     name: str = Field(
#         min_length=3,
#         max_length=40
#     )

#     price: float = Field(
#         ge=0
#     )

#     quantity: int = Field(
#         ge=1
#     )

#     category: str = Field(
#         default="General"
#     )

#     discount: float | None = Field(
#         default=None,
#         ge=0,
#         le=100
#     )


# @app.post("/products")
# def products(product:Product):
#     return{
#         "msg":"Successfull Connection!!!",
#         "product":product
#     }


# default_factory

class cart(BaseModel):
    items: list[str] = Field(
        default_factory=list
    )

# Pydantic Validators

# this is basically use for creating custom validation conditions 

class student(BaseModel):
    name:str

    @field_validator("name")
    @classmethod
    def validate_name(cls,value):
        if not value.isalpha():
            raise ValueError("Enter the name only in Alphabets")
        return value

class Product(BaseModel):
    name:str
    orignal_price:float
    discount_price:float

    @field_validator("orignal_price")
    @classmethod
    def check_price(cls,value):
        if value<0:
            raise ValueError("Value less than 0 is not acceptable")
        return value
    
    @field_validator("discount_price")
    @classmethod
    def check_price(cls,value):
        if value<0:
            raise ValueError("Value less than 0 is not acceptable")
        return value

    @model_validator(mode="after")
    def value_check(self):
        if self.orignal_price <= self.discount_price:
            raise ValueError("discount price must be less than orignal price")
        return self

@app.post("/products")
def product(products:Product):
    return {
        "name":products.name,
        "original_price":products.orignal_price,
        "discount_price":products.discount_price
    }