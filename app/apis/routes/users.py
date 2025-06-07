from fastapi import APIRouter, HTTPException, Request
from sqlalchemy.exc import IntegrityError

from app import serializers
from app.db import models
from app.db.session import get_db_session

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", summary="Create User")
def create_user(request: Request, user: serializers.CreateUser):
    with get_db_session() as db:
        try:
            db_user = models.User(**user.model_dump())
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return db_user
        except IntegrityError as e:
            db.rollback()
            if "ix_users_email" in str(e.orig):
                raise HTTPException(
                    status_code=409, detail="A user with this email already exists."
                )
            raise HTTPException(
                status_code=500, detail="An unexpected database error occurred."
            )
