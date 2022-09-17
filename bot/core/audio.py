from .base import AudioBase
from aiogram import types, Bot
import datetime
import os


class VideoNote(AudioBase):
    def __init__(self, ms: types.Message, bot: Bot):
        self.message = ms
        self.file_id = ms.video_note.file_id
        self.bot = bot

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

    async def get_file(self):
        file = await self.bot.get_file(self.file_id)
        file_path = file.file_path
        _, ext = os.path.splitext(file_path)
        
        cache_name = f"cache/{}"

    async def recognize_speech(self):
        pass


async def recognize(audio_fragment: AudioBase):
    await audio_fragment.recognize_speech()


async def get_