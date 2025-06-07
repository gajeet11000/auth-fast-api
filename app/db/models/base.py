from sqlalchemy import Column, DateTime
from datetime import datetime

from app.db.session import Base


class TimestampedModel(Base):
    """Abstract base model with timestamp fields"""

    __abstract__ = True

    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
    )
