import time
import datetime
from aiogram import types, exceptions, executor
from bot.settings import get_settings
from logging import getLogger
from .base import dp

logger = getLogger(__name__)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    pass


@dp.message_handler(commands=['help'])
async def print_help_info(message: types.Message):
    pass
