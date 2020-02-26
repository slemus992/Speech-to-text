#cffi
#sounddevice

import speech_recognition as sr
# https://realpython.com/python-speech-recognition/ tuto
r = sr.Recognizer()

h = sr.AudioFile('audios/jackhammer.wav')
with h as source:
    audio = r.record(source)
#    audio = r.record(source, duration=4) # para ambiente r.adjust_for_ambient_noise(source)
    type(audio)
    print(audio)
    t = r.recognize_google(audio)
    print(t)