from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from datetime import datetime, timezone
from app.db.base import Base


class Score(Base):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    wpm = Column(Float)
    accuracy = Column(Float)
    errors = Column(Integer)

    duration = Column(Integer)

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )