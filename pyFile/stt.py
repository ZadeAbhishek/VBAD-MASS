from os import write
import pyaudio
import speech_recognition as sr
from threading import Timer
from pynput import keyboard


textArray = ''
val = 'start'


def Convertwrite(source):
    recognizer = sr.Recognizer()
    global textArray
    recognizer.adjust_for_ambient_noise(source, duration=0.5)
    audio = recognizer.listen(source,10,60)
    textArray = '' + (recognizer.recognize_google(audio))
    textArray += ' '
    print(textArray)
    listenkey() 


# Limitation to my observation till know is that the if not correct work is listen it will throw error 
# this error some bring the control out og program

def start() :
    global textArray
    while val == 'start':
        with sr.Microphone() as source :
            print('Listining.........')
            Convertwrite(source)
            
            

def listenkey():
    print(" \n Press Ctrl to start or continue Recording \n Press esc to Stop")
    with keyboard.Events() as events:
         for event in events:
             if event.key == keyboard.Key.ctrl:
               start()
             if event.key == keyboard.Key.esc:
                global val
                val = 'stop'
                return textArray      

# Very first function to run when intialized   
textValue = listenkey()
print(textValue)        

# The event listener will be running in this block

   

# init_rec = sr.Recognizer()
# print("Let's speak!!")
# with sr.Microphone() as source:
#     audio_data = init_rec.record(source, duration=5)
#     print("Recognizing your text.............")
#     text = init_rec.recognize_google(audio_data)
#     print(text)