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
    id = Column(sqlalchemy.Integer, primary_key=True, nullable=False, autoincrement=True)
    chat_id = Column(sqlalchemy.Integer, nullable=False)
    username = Column(sqlalchemy.String, nullable=False)
    last_use = Column(sqlalchemy.DateTime, nullable=False, default=datetime.utcnow(), onupdate=datetime.utcnow())


class ActionInfo(Base):
    id = Column(sqlalchemy.Integer, primary_key=True)
    user_id = Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("user.id"))
    user_action = Column(sqlalchemy.Enum(ActionType, name='user_action'), nullable=False)
    date = Column(sqlalchemy.DateTime, nullable=False, default=datetime.utcnow())
    response_time = Column(sqlalchemy.Float, nullable=True)


class Preferences(Base):
    id = Column(sqlalchemy.Integer, primary_key=True)
    user_id = Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("user.id"))
    transcription_limit = Column(sqlalchemy.Integer, nullable=False, default=0)
