from bot.handlers.base import dp
from aiogram import executor
import logging
from bot.handlers.db_utils import create_user_if_not_exists, get_session, post_action
from bot.models.db import ActionType

logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S'
)


if __name__ == '__main__':
    session = get_session()
    create_user_if_not_exists(session, 666)
    i = post_action(session, 666, ActionType.RANDOM_ACTION)
    print(i)
    # executor.start_polling(dp, skip_updates=True)
