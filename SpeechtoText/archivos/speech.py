import speech_recognition as sr

filename = "LongWelcome.wav"

# Initializing the recognizer
recognizer = sr.Recognizer()

#open the file
with sr.AudioFile(filename) as source:
  #listen for the data (load audio to memory)
  audio_data = recognizer.record(source)
  #recognize (convert from speech to text)
  text = recognizer.recognize_google(audio_data)
  print(text)
    
