from bot.handlers.base import dp
from aiogram import executor
import logging
from bot.handlers.db_utils import create_user_if_not_exists, get_session

logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S'
)


if __name__ == '__main__':
    # executor.start_polling(dp, skip_updates=True)
    with get_session() as session:
        create_user_if_not_exists(session, 10)
        session.flush()
