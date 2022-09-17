from .base import AudioBase
from aiogram import types, Bot
from logging import getLogger
import datetime
import os


logger = getLogger(__name__)


class VideoNote(AudioBase):
    def __init__(self, ms: types.Message, bot: Bot):
        self.message = ms
        self.file_id = ms.video_note.file_id
        self.bot = bot
        self.ext = ".mp4"

    async def get_file(self):
        file = await self.bot.get_file(self.file_id)
        file_path = file.file_path
        _, ext = os.path.splitext(file_path)


    async def recognize_speech(self):
        pass


class Audio(AudioBase):
    def __init__(self, ms: types.Message, bot: Bot):
        self.message = ms
        self.file_id = ms.audio.file_id
        self.bot = bot
        self.ext = ".mp3"

    async def get_file(self):
        file = await self.bot.get_file(self.file_id)
        file_path = file.file_path
        _, ext = os.path.splitext(file_path)

    async def recognize_speech(self):
        pass


class Voice(AudioBase):
    def __init__(self, ms: types.Message, bot: Bot):
        self.message = ms
        self.file_id = ms.voice.file_id
        self.bot = bot
        self.ext = ".ogg"

    async def get_file(self):
        file = await self.bot.get_file(self.file_id)
        file_path = file.file_path
        _, ext = os.path.splitext(file_path)

        cache_path = f"cache/voice_{datetime.datetime.utcnow()}.ogg"
        await self.bot.download_file(file_path, cache_path)
        if os.path.exists(cache_path):
            logg

    async def recognize_speech(self):
        pass


async def recognize(audio_fragment: AudioBase):
    await audio_fragment.recognize_speech()


async def get_