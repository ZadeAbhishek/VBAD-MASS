# This file the main file for initialization from this file we are going 
# basically control most of the speech-to-text-to-speech function
# This is kind of script file and mostly original made by Group 2 :):):)

#from stt import listenkey
#from tts import tts
from .paraCheck import checkparaSimilarity ,similarity
from .preprocessing import preprocessing
from .checkKeywords import checkKeyword
from .cfgParser import checkGrammer
from .model import model

# Conside this as teachers data
def checkinit(value,teachersAnswers,teacherKeyword):
    teachersAnswers = "The git pull command is used to fetch and download content from a remote repository and immediately update the local repository to match that content. Merging remote upstream changes into your local repository is a common task in Git-based collaboration work flows. The git pull command is actually a combination of two other commands, git fetch followed by git merge. In the first stage of operation git pull will execute a git fetch scoped to the local branch that HEAD is pointed at. Once the content is downloaded, git pull will enter a merge workflow. A new merge commit will be-created and HEAD updated to point at the new commit."
    teacherKeyword = "pull fetch Merge" 
    teacherKeyword = teacherKeyword.lower()
    # consider this as Student date
    # # Know we are listnig the student 
    # # value = listenkey()
    
    # # Saving the audio file
    # # The idea is to save in database and direcly link to page
    # #name = input("Please Provide name for audio file to save: ")
    # #tts(value, name)
    # #print('saved.......')
    
    # # Checking the similarity between the Student and teacher Answer (Presprocessing is not working)
    similarAnswer = checkparaSimilarity(teachersAnswers,value)
    similarit = similarity(teachersAnswers,value)
    
    # Know preprocessing the text of Student and teacher (For teacher this is still debetable to consider the preprocessing)
    # But for know we are preprocesing the both
    value = preprocessing(value)
    teachersAnswers = preprocessing(value)
    
    # Checking keywords similarity return percentages simlar
    keyWordtest = checkKeyword(value,teacherKeyword)
    
    # Checking grammer for Student Answer
    GrammerScore  = checkGrammer(value)
    
    # Printing Total Result of Grammer
    #print('........Score..........')
    #print('td-idf Similarity       : {} '.format(similarAnswer))
    #print('Vector Similarity       : {} '.format(similarit))
    #print('Keywords Found          : {} '.format(keyWordtest))
    #print('Grammer Score           : {} '.format(GrammerScore))
    #print('.......................')
    
    # Sending this Score values to final naive bayes classifiers
    result = []
    result.append(float(similarAnswer))
    result.append(float(similarit))
    result.append(float(keyWordtest))
    result.append(float(GrammerScore))
    finalresult =  model(result)

    return similarAnswer, similarit, keyWordtest, GrammerScore, finalresult