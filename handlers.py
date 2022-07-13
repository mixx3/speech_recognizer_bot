import logging
import time
from aiogram import Bot, Dispatcher, types, exceptions, executor
from configparser import ConfigParser
from core import AUDIO_ROOT, recognize_speech, mp3_to_vaw, ogg_to_vaw
import random
import os

config = ConfigParser()
config.read('auth.ini')
API_TOKEN = config['auth_tg']['bot_token']

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    with open('templates/start.html', 'r') as file:
        await message.reply(file.read(), parse_mode=types.ParseMode.HTML)


@dp.message_handler(content_types=types.ContentType.VOICE)
async def voice_download(ms: types.Message):
    file_id = ms.voice.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    cache_name = f"{AUDIO_ROOT}/{random.randint(1,1000)}"
    ext = '.ogg'
    cache_path = f"{cache_name}{ext}"
    print('voice recieved', cache_path)
    await bot.download_file(file_path, cache_path)
    if os.path.exists(cache_path):
        ogg_to_vaw(cache_path)
        text = recognize_speech(f"{cache_name}.wav")
        os.remove(f"{cache_name}.wav")
    else:
        raise OSError("path not found or file is not downloaded yet")
    await bot.send_message(ms.chat.id, text)


@dp.message_handler(content_types=types.ContentType.AUDIO)
async def audio_download(ms: types.Message):
    file_id = ms.audio.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    cache_name = f"{AUDIO_ROOT}/{random.randint(1,1000)}"
    ext = '.mp3'
    cache_path = f"{cache_name}{ext}"
    print('voice recieved', cache_path)
    await bot.download_file(file_path, cache_path)
    if os.path.exists(cache_path):
        mp3_to_vaw(cache_path)
        text = recognize_speech(f"{cache_name}.wav")
        os.remove(f"{cache_name}.wav")
    else:
        raise OSError("path not found or file is not downloaded yet")
    await bot.send_message(ms.chat.id, text)


@dp.message_handler(commands=['help'])
async def print_help_info(message: types.Message):
    with open('templates/help.html', 'r') as file:
        await message.reply(file.read())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
