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