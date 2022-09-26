import datetime
from bot.models.db import User, ActionInfo, ActionType
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from bot.settings import get_settings


def get_session():
    engine = create_engine(get_settings().DB_DSN)
    return Session(bind=engine, autocommit=True)


async def create_user_if_not_exists(session: Session, tg_id: int) -> int:
    res = session.query(User).filter(User.chat_id == tg_id)
    user = User(chat_id=tg_id)
    if not res.one_or_none():
        session.add(user)
    else:
        res.update(dict(chat_id=tg_id, last_use=datetime.datetime.utcnow()))
    session.flush()
    return user.id


async def post_action(session: Session, user_tg_id: int, action: str) -> None:
    user_id = await create_user_if_not_exists(session, user_tg_id)
    user.update(dict(chat_id=user_tg_id, last_use=datetime.datetime.utcnow()))
    db_action = ActionInfo(user_id=user_id, user_action=action, date=datetime.datetime.utcnow())
    session.add(db_action)
    session.flush()

