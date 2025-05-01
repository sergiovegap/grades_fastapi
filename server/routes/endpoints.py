from fastapi import APIRouter, Body
from ..users.models import User

router = APIRouter(prefix="/user", tags=["User"])

# Example
superheroe = {
    "name": "Wanda", "lastname": "Maximoff", "role": "superhero", "subjects": 4
}

# Create user
@router.post("/")
def create_user(user: User):
    return superheroe
    # return {user.name: "Wanda", user.lastname: "Maximoff", user.role: "superhero", user.subjects: 4}

# Get user
@router.get("/")
def get_user(id: int, user: User):
    return {"id": id, "name": user.name, "lastname": user.lastName, "role": user.role, "subjects": user.subjects}


