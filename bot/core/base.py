from abc import ABC, abstractmethod
from aiogram import types


class AudioBase(ABC):
    @abstractmethod
    async def recognize_speech(self):
        ...

    @abstractmethod
    async def get_file(self):
        ...