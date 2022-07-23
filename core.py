import speech_recognition as sr
import sys
from os import path
import os
from pydub import AudioSegment
import moviepy.editor as mp
import logging

logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S'
)
log = logging.getLogger(__name__)

FILE_ROOT = path.join(path.dirname(path.realpath(__file__)), 'cache')


def recognize_speech(audio_path: str) -> str:
    r = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = r.record(source)
    log.info('speech recognized')
    return r.recognize_google(audio, language='ru')


def to_wav(file_path: str) -> str:
    """
    Encodes audio/video file to .wav format
    :param file_path: path to file
    :return: file
    """
    full_name, exc = os.path.splitext(file_path)
    if exc == ".ogg":
        log.info('ogg file recieved')
        sound = AudioSegment.from_ogg(file_path)
        with open(f"{full_name}.wav", 'wb') as outfile:
            sound.export(outfile, format='wav')
    elif exc == ".mp4":
        log.info('mp4 file recieved')
        video = mp.VideoFileClip(file_path)
        video.audio.write_audiofile(f"{full_name}.ogg")
        sound = AudioSegment.from_ogg(f"{full_name}.ogg")
        os.remove(f"{full_name}.ogg")
        with open(f"{full_name}.wav", 'wb') as outfile:
            sound.export(outfile, format='wav')
    elif exc == ".mp3":
        log.info('mp3 file recieved')
        sound = AudioSegment.from_mp3(file_path)
        with open(f"{full_name}.wav", 'wb') as outfile:
            sound.export(outfile, format='wav')
    elif exc == ".wav":
        log.warning("trying to code wav to wav")
        pass
    else:
        log.error("other file format recieved: %s", file_path)
        raise AttributeError("file can not be exported to wav")
    os.remove(file_path)
    return f"{full_name}.wav"


def recognize_input(input_path: str) -> str:
    new_path = to_wav(input_path)
    return recognize_speech(new_path)
