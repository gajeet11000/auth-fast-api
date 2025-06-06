from fastapi import APIRouter, Request
from app.serializers.users import CreateUser

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", summary="Create User")
def create_user(request: Request, user: CreateUser):
    return {"message": "User created successfully", "user": user}
