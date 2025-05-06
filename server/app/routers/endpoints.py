from fastapi import APIRouter, Depends
from ..database.database import get_db
from sqlalchemy.orm import Session
from ..models.users import Professor

router = APIRouter(prefix="/user", tags=["User"])

# Example
# superhero = {
#     "name": "Wanda", "lastname": "Maximoff", "role": "superhero", "subjects": 4
# }

# Create user
@router.post("/superhero")
def create_user():
    # return user
    return {"name": "Wanda", "lastname": "Maximoff", "role": "superhero", "subjects": 4}

# Get user
# @router.post("/professor")
# def get_user(id: id, user: Professor) -> Professor:
#     return Professor
    # return {"id": id, "name": Professor.name, "lastname": Professor.lastName}


# @router.get("/professors")
# def get_professors(db: Session = Depends(get_db)):
#     data = db.query(Professor).all()
#     return data