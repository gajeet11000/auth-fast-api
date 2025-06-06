from fastapi import FastAPI
from .apis import api_router
from .db.session import engine, Base
from .db.models import *  # noqa: F403

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(api_router)
