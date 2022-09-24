import datetime
from bot.models.db import User, ActionInfo, ActionType
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from bot.settings import get_settings


def get_session():
    engine = create_engine(get_settings().DB_DSN)
    return Session(bind=engine, autocommit=True)


def create_user_if_not_exists(session: Session, tg_id: int):
    res = session.query(User).filter(User.telegram_id == tg_id).one_or_none()
    if not res:
        user = User(telegram_id=tg_id)
        session.add(user)
    else:
        res.update()



