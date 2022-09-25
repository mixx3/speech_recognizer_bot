from aiogram import Bot, Dispatcher
from bot.settings import get_settings
from aiogram import types
from bot.core.audio import Audio, Voice, VideoNote
from bot.core.base import recognize
from logging import getLogger
from .db_utils import create_user_if_not_exists, get_session, post_action
from bot.models.db import ActionType


logger = getLogger(__name__)
bot = Bot(get_settings().BOT_TOKEN)
dp = Dispatcher(bot)
session = get_session()


@dp.message_handler(content_types=[types.ContentType.VOICE])
async def recognize_voice(ms: types.Message):
    await post_action(session, ms.chat.id, ActionType.VOICE_MESSAGE)
    voice = Voice(ms, bot)
    text = await recognize(voice)
    if not text:
        await bot.send_message(ms.chat.id, "No text to transcribe")
        logger.info(f"Invalid vioce message from {ms.chat.as_json()}")
    await bot.send_message(ms.chat.id, text)


@dp.message_handler(content_types=[types.ContentType.AUDIO])
async def recognize_audio(ms: types.Message):
    await post_action(session, ms.chat.id, ActionType.AUDIO_FILE)
    audio = Audio(ms, bot)
    text = await recognize(audio)
    if not text:
        await bot.send_message(ms.chat.id, "No text to transcribe")
        logger.info(f"Invalid audio message from {ms.chat.as_json()}")
    await bot.send_message(ms.chat.id, text)


@dp.message_handler(content_types=[types.ContentType.VIDEO_NOTE])
async def recognize_video_note(ms: types.Message):
    await post_action(session, ms.chat.id, ActionType.VIDEO_NOTE)
    video_note = VideoNote(ms, bot)
    text = await recognize(video_note)
    if not text:
        await bot.send_message(ms.chat.id, "No text to transcribe")
        logger.info(f"Invalid video note from {ms.chat.as_json()}")
    await bot.send_message(ms.chat.id, text)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await create_user_if_not_exists(session, message.chat.id)
    await message.reply(
    """Привет.\nЭто бот для транскрипции голосовых сообщений, аудиозаписей и кружков в телеграме.\nЕсли есть вопросы, пиши /help"""
    )


@dp.message_handler(commands=['help'])
async def print_help_info(message: types.Message):
    await post_action(session, message.chat.id, ActionType.RANDOM_ACTION)
    await message.reply(
    """Aхаахха никто тебе не поможет)\nМожешь мне на почту написать \nparfenov.ma21@physics.msu.ru"""
    )
