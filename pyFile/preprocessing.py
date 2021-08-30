# This folder is for prepossing the text given by students mostly student sometimes for teacher 
# Since we donnt know the what is my output voice or text 

import pandas as pd
import string 
import nltk
from nltk.corpus import stopwords as stopword
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
import re
# Below is sample for debug donot conside that we have copy this :) :)
# data = "Asymptotic Analysis is the big idea that handles above issues in analyzing algorithms. In Asymptotic Analysis, we evaluate the performance of an algorithm in terms of input size (we don’t measure the actual running time). We calculate, how the time (or space) taken by an algorithm increases with the input size.For example, let us consider the search problem (searching a given item) in a sorted array. One way to search is Linear Search (order of growth is linear) and the other way is Binary Search (order of growth is logarithmic). To understand how Asymptotic Analysis solves the above mentioned problems in analyzing algorithms, let us say we run the Linear Search on a fast computer A and Binary Search on a slow computer B and we pick the constant values for the two computers so that it tells us exactly how long it takes for the given machine to perform the search in seconds. Let’s say the constant for A is 0.2 and the constant for B is 1000 which means that A is 5000 times more powerful than B. For small values of input array size n, the fast computer may take less time. But, after a certain value of input array size, the Binary Search will definitely start taking less time compared to the Linear Search even though the Binary Search is being run on a slow machine. The reason is the order of growth of Binary Search with respect to input size is logarithmic while the order of growth of Linear Search is linear Asymptotic Analysis is not perfect, but that’s the best way available for analyzing algorithms. For example, say there are two sorting algorithms that take 1000nLogn and 2nLogn time respectively on a machine. Both of these algorithms are asymptotically same (order of growth is nLogn). So, With Asymptotic Analysis, we can’t judge which one is better as we ignore constants in Asymptotic Analysis.Also, in Asymptotic analysis, we always talk about input sizes larger than a constant value. It might be possible that those large inputs are never given to your software and an algorithm which is asymptotically slower, always performs better for your particular situation. So, you may end up choosing an algorithm that is Asymptotically slower but faster for your software."


def preprocessing(data):
    
    # lowering the datasets 
    data = data.lower()
    # removing punctuations ex.(? !)
    string.punctuation
    def remove_punctuation(text):
       punctuationfree="".join([i for i in text if i not in string.punctuation])
       return punctuationfree

    #storing the puntuation free text
    data = remove_punctuation(data)
    print("\n .......................................Removing punctuation ...............................................................")
    print(data)

  

    #Removing Stops words 
    stop_words = set(stopword.words('english'))
    word_tokens = word_tokenize(data)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
    stopwords = nltk.corpus.stopwords.words('english')
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
           filtered_sentence.append(w)
 
    print(word_tokens)

    print(".......................Filter ...................................................")
    print(filtered_sentence)
    combined_data = TreebankWordDetokenizer().detokenize(filtered_sentence)
    print(combined_data)
    return combined_data
