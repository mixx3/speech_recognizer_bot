from aiogram import types
import os
import datetime
from logging import getLogger
import speech_recognition as sr

logger = getLogger(__name__)


class AudioBase:
    def __init__(self):
        self.file_path = ""
        self.bot = None
        self.file_id = None
        self.ext = ".ogg"

    async def get_file(self):
        file = await self.bot.get_file(self.file_id)
        file_path = file.file_path
        _, ext = os.path.splitext(file_path)
        cache_path = os.path.realpath(f"cache/voice_{datetime.datetime.utcnow()}{self.ext}")
        await self.bot.download_file(file_path, cache_path)
        logger.debug(f"file received, {cache_path}")
        self.file_path = cache_path

    async def to_vaw(self):
        pass

    async def recognize_speech(self):
        await self.to_vaw()
        assert self.file_path.endswith(".wav")
        r = sr.Recognizer()
        with sr.AudioFile(self.file_path) as source:
            audio = r.record(source)
        logger.info('speech recognized')
        return r.recognize_google(audio, language='ru')


async def recognize(audio_fragment: AudioBase):
    return await audio_fragment.recognize_speech()
