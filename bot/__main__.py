from bot.handlers.base import dp
from aiogram import executor
import logging


logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S'
)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

