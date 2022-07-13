import speech_recognition as sr
import sys
from os import path
import os
from pydub import AudioSegment
AUDIO_ROOT = path.join(path.dirname(path.realpath(__file__)), 'cache')


def recognize_speech(path: str):
    r = sr.Recognizer()
    with sr.AudioFile(path) as source:
        audio = r.record(source)
    return r.recognize_google(audio, language='ru')


def mp3_to_vaw(mp3_fp: str):
    assert mp3_fp.split('.')[-1] == "mp3"
    sound = AudioSegment.from_mp3(mp3_fp)
    os.remove(mp3_fp)
    with open(f"{ogg_fp.split('.')[0]}.wav", 'wb') as outfile:
        sound.export(outfile, format='wav')


def ogg_to_vaw(ogg_fp: str):
    assert ogg_fp.split('.')[-1] == "ogg"
    sound = AudioSegment.from_ogg(ogg_fp)
    os.remove(ogg_fp)
    with open(f"{ogg_fp.split('.')[0]}.wav", 'wb') as outfile:
        sound.export(outfile, format='wav')


if __name__ == '__main__':
    print(os.environ['PATH'])
    print(recognize_speech("/Users/new/PycharmProjects/speech_recognizer/cache/800.wav"))