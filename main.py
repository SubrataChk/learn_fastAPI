from fastapi import FastAPI

app = FastAPI()



#Post:

@app.post("/create_user")
def create_user(name: str, age: int):
    return {
        "name" : name,
        "age" : age
    }



# Query Parameter:

# @app.get("/items")
# def items(name : str = None, price : int = 0):
#     return {"name": name, "price": price}


# @app.get("/users")
# def user_search(name: str = "My Friend"):
#     return {"message": f"Hello, {name}"}




# #Parameter:

# @app.get("/users/{name}")
# def user_search(name: int  | str = None):
#     return {"message": f"Hello, {name}"}




# @app.get("/new")
# def home():
#     return {"message": "Hello, World!"}


# @app.get("/users")
# def users():
#     return {"users": ["Subrata", "John", "Alice", "Bob"]}

# @app.get("/about")
# def about():
#     return {"message": "This is a FastAPI application."}