from bot.handlers.base import dp
from aiogram import executor
import logging
from bot.handlers.db_utils import create_user_if_not_exists, get_session, post_action
from bot.models.db import ActionType


logging.basicConfig(
    filename=f'logger_{__name__}.log',
    level=logging.DEBUG,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
