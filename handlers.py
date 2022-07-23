import logging
import time
from aiogram import Bot, Dispatcher, types, exceptions, executor
from configparser import ConfigParser
from core import FILE_ROOT, recognize_input
import random
import os

config = ConfigParser()
config.read('auth.ini')
API_TOKEN = config['auth_tg']['bot_token']

logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S'
)
log = logging.getLogger(__name__)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    with open('templates/start.html', 'r') as file:
        log.info("new user!")
        await message.reply(file.read(), parse_mode=types.ParseMode.HTML)


@dp.message_handler(content_types=[types.ContentType.VOICE,
                                   types.ContentType.AUDIO,
                                   types.ContentType.VIDEO_NOTE])
async def voice_transcribe(ms: types.Message):
    text = "cannot extract file from message"
    if ms.voice:
        file_id = ms.voice.file_id
    elif ms.audio:
        file_id = ms.audio.file_id
    elif ms.video_note:
        file_id = ms.video_note.file_id
    else:
        await bot.send_message(ms.chat.id, text)
    file = await bot.get_file(file_id)
    file_path = file.file_path
    _, ext = os.path.splitext(file_path)
    if ext == ".oga":
        ext = ".ogg"
    cache_name = f"{FILE_ROOT}/{random.randint(1,1000)}"
    cache_path = f"{cache_name}{ext}"
    await bot.download_file(file_path, cache_path)
    if os.path.exists(cache_path):
        log.info("file %s recieved", cache_path)
        text = recognize_input(cache_path)
    else:
        raise OSError("path not found or file is not downloaded yet")
    await bot.send_message(ms.chat.id, text)


@dp.message_handler(commands=['help'])
async def print_help_info(message: types.Message):
    with open('templates/help.html', 'r') as file:
        await message.reply(file.read())
