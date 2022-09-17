from .base import AudioBase
from aiogram import types, Bot
from logging import getLogger
from pydub import AudioSegment
import moviepy.editor as mp
import speech_recognition as sr
import datetime
import os


logger = getLogger(__name__)


class VideoNote(AudioBase):
    def __init__(self, ms: types.Message, bot: Bot):
        super().__init__()
        self.message = ms
        self.file_id = ms.video_note.file_id
        self.bot = bot
        self.ext = ".mp4"
        self.file_path = ""

    async def to_vaw(self):
        await self.get_file()
        file_name, _ = os.path.splitext(self.file_path)
        logger.debug(".mp4 file received")
        video = mp.VideoFileClip(self.file_path)
        video.audio.write_audiofile(f"{file_name}.ogg")
        sound = AudioSegment.from_ogg(f"{file_name}.ogg")
        os.remove(f"{file_name}.ogg")
        with open(f"{file_name}.wav", "wb") as outfile:
            self.sound.export(outfile, format="wav")
        os.remove(self.file_path)
        self.file_path = f"{file_name}.wav"


class Audio(AudioBase):
    def __init__(self, ms: types.Message, bot: Bot):
        super().__init__()
        self.message = ms
        self.file_id = ms.audio.file_id
        self.bot = bot
        self.ext = ".mp3"
        self.file_path = ""

    async def to_vaw(self):
        await self.get_file()
        file_name, _ = os.path.splitext(self.file_path)
        sound = AudioSegment.from_mp3(file_path)
        with open(f"{file_name}.wav", "wb") as outfile:
            sound.export(outfile, format="wav")
        os.remove(self.file_path)
        self.file_path = f"{file_name}.wav"

class Voice(AudioBase):
    def __init__(self, ms: types.Message, bot: Bot):
        super().__init__()
        self.message = ms
        self.file_id = ms.voice.file_id
        self.bot = bot
        self.ext = ".ogg"
        self.file_path = ""

    async def to_vaw(self):
        await self.get_file()
        logger.debug(".ogg file received")
        sound = AudioSegment.from_ogg(self.file_path)
        file_name, _ = os.path.splitext(self.file_path)
        with open(f"{file_name}.wav", "wb") as outfile:
            sound.export(outfile, format="wav")
        os.remove(self.file_path)
        self.file_path = f"{file_name}.wav"

