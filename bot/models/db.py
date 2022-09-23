from .base import Base
from sqlalchemy import Column
from datetime import datetime
import sqlalchemy.orm
import enum


class ActionType(str, enum.Enum):
    VOICE_MESSAGE: str = "voice_message"
    VIDEO_NOTE: str = "video_note"
    AUDIO_FILE: str = "audio_file"
    RANDOM_ACTION: str = "invalid_action"


class User(Base):
    id = Column(sqlalchemy.Integer, primary_key=True, nullable=False)
    telegram_id = Column(sqlalchemy.Integer, nullable=False)
    last_use = Column(sqlalchemy.DateTime, nullable=False, default=datetime.utcnow(), onupdate=datetime.utcnow())


class ActionInfo(Base):
    id = Column(sqlalchemy.Integer, primary_key=True)
    user_id = Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("user.id"))
    action = Column(sqlalchemy.Enum(ActionType, name='action'), nullable=False)
    date = Column(sqlalchemy.DateTime, nullable=False, default=datetime.utcnow())
    response_time = Column(sqlalchemy.Float, nullable=True)
