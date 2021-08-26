from stt import listenkey
from tts import tts

value = listenkey()
name = input("Please Provide name for audio file to save: ")
tts(value, name)
