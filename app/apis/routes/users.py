from fastapi import APIRouter, Request

from app.db import models
from app.db.session import get_db_session
from app import serializers

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", summary="Create User")
def create_user(request: Request, user: serializers.CreateUser):
    with get_db_session() as db:
        db_user = models.User(**user.model_dump())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
