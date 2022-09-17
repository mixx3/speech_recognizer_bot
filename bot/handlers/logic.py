from .base import dp, bot
from aiogram import types
from bot.core.audio import Audio, Voice, VideoNote, recognize


@dp.message_handler(content_types=[types.ContentType.VOICE])
async def recognize_voice(ms: types.Message):
    voice = Voice(ms, bot)
    text = await recognize(voice)


@dp.message_handler(content_types=[types.ContentType.AUDIO])
async def recognize_audio(ms: types.Message):
    audio = Audio(ms, bot)
    text = await recognize(audio)


@dp.message_handler(content_types=[types.ContentType.VIDEO_NOTE])
async def recognize_video_note(ms: types.Message):
    video_note = VideoNote(ms, bot)
    text = await recognize(video_note)
