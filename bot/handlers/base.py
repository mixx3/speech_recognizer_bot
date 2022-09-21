from aiogram import Bot, Dispatcher
from bot.settings import get_settings
from aiogram import types
from bot.core.audio import Audio, Voice, VideoNote
from bot.core.base import recognize
from logging import getLogger


logger = getLogger(__name__)
bot = Bot(get_settings().BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(content_types=[types.ContentType.VOICE])
async def recognize_voice(ms: types.Message):
    voice = Voice(ms, bot)
    text = await recognize(voice)
    logger.debug("voice message!")
    logger.debug(text)
    if not text:
        await bot.send_message(ms.chat.id, "nonono")
    await bot.send_message(ms.chat.id, text)


@dp.message_handler(content_types=[types.ContentType.AUDIO])
async def recognize_audio(ms: types.Message):
    audio = Audio(ms, bot)
    text = await recognize(audio)
    logger.debug(text)
    if not text:
        await bot.send_message(ms.chat.id, "nonono")
    await bot.send_message(ms.chat.id, text)


@dp.message_handler(content_types=[types.ContentType.VIDEO_NOTE])
async def recognize_video_note(ms: types.Message):
    video_note = VideoNote(ms, bot)
    text = await recognize(video_note)
    await bot.send_message(ms.chat.id, text)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi")


@dp.message_handler(commands=['help'])
async def print_help_info(message: types.Message):
    pass
