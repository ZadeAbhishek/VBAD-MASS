from typing import Text
from gtts import gTTS
import os

def tts(text,name):
    tts = gTTS(text)
    print('Saving Mp3......')
    tts.save("%s.mp3" % os.path.join("../mp3",name))
    print('saved')
    return