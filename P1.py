# from fastapi import FastAPI, status
# from pydantic import BaseModel

# # 1. Start the FastAPI Engine
# app = FastAPI()

# # 2. Define what a "User" should look like (Data Validation contract)
# class User(BaseModel):
#     id: int
#     name: str

# # 3. Create a GET Route (Retrieves data, Safe action, No request body)
# @app.get("/users")
# def get_users():
#     # Returning a structured JSON response
#     return [
#         {"id": 1, "name": "Alice"},
#         {"id": 2, "name": "Bob"}
#     ]

# # 4. Create a POST Route (Creates a resource, returns 201 Created status code)
# @app.post("/users", status_code=status.HTTP_201_CREATED)
# def create_user(user: User):
#     # This processes the payload completely stateless
#     return {
#         "status": "success",
#         "message": "User created in memory!",
#         "data": user
#     }

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

app = FastAPI(title="REST API Fundamentals")

# ---------- DATA MODELS ----------

class User(BaseModel):
    name: str
    email: EmailStr

class UserResponse(User):
    id: int

# In-memory "database" (just a list, resets on restart — stays stateless per request)
users: list[UserResponse] = [
    UserResponse(id=1, name="Alice", email="alice@example.com"),
    UserResponse(id=2, name="Bob", email="bob@example.com"),
]
next_id = 3

# ---------- ROUTES ----------

@app.get("/")
def health_check():
    return {"status": "ok", "message": "Server is running"}

# GET /users -> Read all users
@app.get("/users", response_model=list[UserResponse])
def get_users():
    return users

# GET /users/{id} -> Read single user
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# POST /users -> Create new user
@app.post("/users", response_model=UserResponse, status_code=201)
def create_user(user: User):
    global next_id
    new_user = UserResponse(id=next_id, name=user.name, email=user.email)
    users.append(new_user)
    next_id += 1
    return new_user