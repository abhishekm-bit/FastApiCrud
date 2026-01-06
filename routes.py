from fastapi import APIRouter
from database import collection
from models import User
from fastapi import HTTPException

router = APIRouter()

@router.post("/users")
def create_user(user: User):
    existing_user = collection.find_one({"email": user.email})

    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    collection.insert_one(user.dict())
    return {"message": "User created successfully"}

@router.get("/users")
def get_users():
    users = list(collection.find({}, {"_id": 0}))
    return users

@router.put("/users/{email}")
def update_user(email: str, user: User):
    collection.update_one({"email": email}, {"$set": user.dict()})
    return {"message": "User updated"}

@router.delete("/users/{email}")
def delete_user(email: str):
    collection.delete_one({"email": email})
    return {"message": "User deleted Successfully..."}
