import speech_recognition as sr
import sys
from os import path
import os
from pydub import AudioSegment
import moviepy.editor as mp

FILE_ROOT = path.join(path.dirname(path.realpath(__file__)), 'cache')


def recognize_speech(audio_path: str) -> str:
    r = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = r.record(source)
    return r.recognize_google(audio, language='ru')


def to_wav(path: str) -> str:
    """
    Encodes audio/video file to .wav format
    :param path: path to file
    :return: file
    """
    full_name, exc = os.path.splitext(path)
    if exc == ".ogg":
        sound = AudioSegment.from_ogg(path)
        os.remove(path)
        with open(f"{full_name}.wav", 'wb') as outfile:
            sound.export(outfile, format='wav')
    elif exc == ".mp4":
        video = mp.VideoFileClip(path)
        video.audio.write_audiofile(f"{full_name}.ogg")
        os.remove(path)
        sound = AudioSegment.from_ogg(f"{full_name}.ogg")
        os.remove(f"{full_name}.ogg")
        with open(f"{full_name}.wav", 'wb') as outfile:
            sound.export(outfile, format='wav')
    elif exc == ".mp3":
        sound = AudioSegment.from_mp3(path)
        with open(f"{full_name}.wav", 'wb') as outfile:
            sound.export(outfile, format='wav')
        os.remove(path)
    elif exc == ".wav":
        pass
    else:
        raise AttributeError("file can not be exported to wav")
    return f"{full_name}.wav"


def recognize_input(path: str) -> str:
    new_path = to_wav(path)
    return recognize_speech(new_path)
