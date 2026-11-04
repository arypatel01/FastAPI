app = FastAPI() -> app is the fats api object 


@app.get("/products") -> .get Handles HTTP GET requests 
                      -> /products denotes the url of get request 


def products():
    return{"products": ["Product 1", "Product 2", "Product 3"]}  -> this is the response of fastapi sends to user 


==================================================================
Introduction To API
==================================================================

A. GET – Retrieve data

B. POST – Create new data

C. PUT – Update existing data

D. PATCH – Partially update data

E. DELETE – Delete data



===> Parameters

1. Path Parameters
A Path Parameter is a value passed directly inside the URL path.
http://127.0.0.1:8000/students/10


3. Query Parameters
A Query Parameter is a value passed after the ? symbol in a URL.
/students?city=Ahmedabad&age=19

student_id: int = 101 -> by default parameter if not given by user this is used to get data 
city: str | None = None -> none is allowed in this case 



1. Receiving JSON using Pydantic BaseModel
    def create_student(student: Student): by using this BaseModel we can get data from frontend in json formate 

2. Using Body() directly
    def get_marks(marks: int = Body()): by using this body() we can directly get the data from frontend 


![alt text](image.png)

