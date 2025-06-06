from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.get("/login", summary="Login endpoint")
def login():
    return {"message": "Login successful"}
