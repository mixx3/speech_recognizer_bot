from abc import ABC, abstractmethod
from aiogram import types


class AudioBase:
    def __init__(self):
        self.file_path = ""

    async def get_file(self):
        file = await self.bot.get_file(self.file_id)
        file_path = file.file_path
        _, ext = os.path.splitext(file_path)
        cache_path = f"cache/voice_{datetime.datetime.utcnow()}.ogg"
        await self.bot.download_file(file_path, cache_path)
        if os.path.exists(cache_path):
            logger.debug(f"file received, {cache_path}")
            self.file_path = cache_path
        raise OSError("Path not found or file is not downloaded")

    async def to_vaw(self):
        pass

    async def recognize_speech(self):
        await self.to_vaw()
        assert self.file_path.endswith(".wav")
        r = sr.Recognizer()
        with sr.AudioFile(self.file_path) as source:
            audio = r.record(source)
        log.info('speech recognized')
        return r.recognize_google(audio, language='ru')


async def recognize(audio_fragment: AudioBase):
    await audio_fragment.recognize_speech()
