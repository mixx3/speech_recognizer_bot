import datetime

from bot.models.db import User, Action, ActionType
from sqlalchemy.orm import Session


def create_user(session: Session, tg_id: int):
    res = session.query(User).filter(User.telegram_id == tg_id).one_or_none()
    if not res:
        user = User(telegram_id=tg_id)
        session.query(User).add(user)
    else:
        res.update()

