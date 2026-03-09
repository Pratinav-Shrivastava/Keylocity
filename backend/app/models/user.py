from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone
from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)

    password_hash = Column(String)

    oauth_provider = Column(String, nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )