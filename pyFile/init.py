# This file the main file for initialization from this file we are going 
# basically control most of the speech-to-text-to-speech function
# Also 

# Things done till now 
# 1.Speech to text implemented (Not proper but working)
# 2. Text to speech (We are able to save mp3 file of recorded text)

# Thing to implememnt next
#  

from stt import listenkey
from tts import tts
from paraCheck import checkparaSimilarity

teachersAnswers = 'The git pull command is used to fetch and download content from a remote repository and immediately update the local repository to match that content. Merging remote upstream changes into your local repository is a common task in Git-based collaboration work flows. The git pull command is actually a combination of two other commands, git fetch followed by git merge. In the first stage of operation git pull will execute a git fetch scoped to the local branch that HEAD is pointed at. Once the content is downloaded, git pull will enter a merge workflow. A new merge commit will be-created and HEAD updated to point at the new commit.'
value = listenkey()
name = input("Please Provide name for audio file to save: ")
tts(value, name)
print('saved.......')
checkparaSimilarity(value,teachersAnswers)