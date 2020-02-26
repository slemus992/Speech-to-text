# importing the module
import pydub
import speech_recognition
# getting the audio file
audio = pydub.AudioSegment.from_wav('Welcome.wav')
# length of the audio in milliseconds
audio_length = len(audio)
print(f'Audio Length: {audio_length}')
# chunk counter
chunk_counter = 1
audio_text = open('audio_text.txt', 'w+')
# setting where to slice the audio
point = 60000
# overlap - remaining audio after slicing
rem = 8000
# initialising variables to track chunks and ending
flag = 0
start = 0
end = 0
# iterating through the audio with incrementing of rem
for i in range(0, 2 * audio_length, point):
   # in first iteration end = rem
   if i == 0:
      start = 0
      end = point
   else:
      # other iterations
      start = end - rem
      end = start + point
   # if end is greater than audio_length
   if end >= audio_length:
      end = audio_length
      # to indicate stop
      flag = 1
   # getting a chunk from the audio
   chunk = audio[start:end]
   # chunk name
   chunk_name = f'chunk_{chunk_counter}'
   # storing the chunk to local storage
   chunk.export(chunk_name, format = 'wav')
   # printing the chunk
   print(f'{chunk_name} start: {start} end: {end}')
   # incrementing chunk counter
   chunk_counter += 1
   # recognising text from the audio
   # initialising the recognizer
   recognizer = speech_recognition.Recognizer()
   # creating a listened audio
   with speech_recognition.AudioFile(chunk_name) as chunk_audio:
      chunk_listened = recognizer.listen(chunk_audio)
   # recognizing content from the audio
   try:
      # getting content from the chunk
      content = recognizer.recognize_google(chunk_listened)
      # writing to the file
      audio_text.write(content + '\n')
   # if not recognized
   except speech_recognition.UnknownValueError:
      print('Audio is not recognized')
   # internet error
   except speech_recognition.RequestError as Error:
      print('Can\'t connect to the internet')
   # checking the flag
   if flag == 1:
      audio_text.close()
   break