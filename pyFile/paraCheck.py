import nltk 
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import gensim
import numpy as np 

# genism help to create bag of word
def checkparaSimilarity(studentAnswer, teacherAnswer):
    fileDocument = []
    answer = teacherAnswer
    TokenizeAnswer = sent_tokenize(answer)
    for token in TokenizeAnswer:
        fileDocument.append(token)
    print(fileDocument)


    word_tokenizer = [[w.lower() for w in word_tokenize(text)] for text in fileDocument]
    print("word tokenizer:.............")
    print(word_tokenizer)

    # creating bag of words with unique id to compare and also it frequnecy of occur
    dictionary = gensim.corpora.Dictionary(word_tokenizer)
    corpus = [dictionary.doc2bow(word_tokens) for word_tokens in word_tokenizer]

    # terfrequency and inverse document frequency this will help to take out important works i.e 
    # words that occurs more time 
    tf_idf = gensim.models.TfidfModel(corpus)
    sameMeter = []
    similarity = gensim.similarities.Similarity('./tf_similarity',tf_idf[corpus], num_features=len(dictionary))



     ## repeating everythng for teacher sane as student 

    fileDocument2 = []
    teacheranswer = studentAnswer
    TokenizeTeacherAnswer = sent_tokenize(teacheranswer)
    for token in TokenizeTeacherAnswer:
        fileDocument2.append(token)
    print(fileDocument2)

    for line in fileDocument2:
      teaher_word_tokenizer = [w.lower() for w in word_tokenize(line)]
      print(teaher_word_tokenizer)
      teacher_word_bow = dictionary.doc2bow(teaher_word_tokenizer)


    teacher_word_tf = tf_idf[teacher_word_bow]
    sum_of_similarity = (np.sum(similarity[teacher_word_tf], dtype=np.float32))
    print(sum_of_similarity)
    percetage_similairty = round(float((sum_of_similarity / len(fileDocument))* 100))
    print('percentage: {}'.format(percetage_similairty))
