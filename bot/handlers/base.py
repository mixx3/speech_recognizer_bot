from aiogram import Bot, Dispatcher
from bot.settings import get_settings


bot = Bot(get_settings().BOT_TOKEN)
dp = Dispatcher(bot)
