# This file the main file for initialization from this file we are going 
# basically control most of the speech-to-text-to-speech function
# This is kind of script file and mostly original made by Group 2 :):):)

from stt import listenkey
from tts import tts
from paraCheck import checkparaSimilarity
from preprocessing import preprocessing
from checkKeywords import checkKeyword

# Conside this as teachers data
teachersAnswers = "The git pull command is used to fetch and download content from a remote repository and immediately update the local repository to match that content. Merging remote upstream changes into your local repository is a common task in Git-based collaboration work flows. The git pull command is actually a combination of two other commands, git fetch followed by git merge. In the first stage of operation git pull will execute a git fetch scoped to the local branch that HEAD is pointed at. Once the content is downloaded, git pull will enter a merge workflow. A new merge commit will be-created and HEAD updated to point at the new commit."
teacherKeyword = "git pull command fetch remote repository Merging remote upstream commit" 
# consider this as Student data
# Know we are listnig the student 
value = listenkey()


# Saving the audio file
# The idea is to save in database and direcly link to page
name = input("Please Provide name for audio file to save: ")
tts(value, name)
print('saved.......')


# Know preprocessing the text of Student and teacher (For teacher this is still debetable to consider the preprocessing)
# But for know we are preprocesing the both
# value = preprocessing(value)
# saveteachersAnswers = preprocessing(value)

# Checking the similarity between the Student and teacher Answer 
checkparaSimilarity(value,teachersAnswers)

# Checking keywords similarity return percentages simlar
checkKeyword(value,teacherKeyword)