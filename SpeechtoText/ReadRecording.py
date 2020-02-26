import speech_recognition as sr


def read(field):
    r = sr.Recognizer()
    file = sr.AudioFile('audios/' + field)
    with file as source:
        audio = r.record(source)
        print(audio)
        audioo = r.recognize_google(audio)
        print(audioo)
        return audioo
