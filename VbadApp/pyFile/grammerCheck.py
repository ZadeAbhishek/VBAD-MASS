

### This folder is under construction :)))))) ####




# In this file code to check gramme has been written 
# Now my idea is to get Raw Answer without preprocessing and and do sentence tokanizing it 
# After toke.... we will check grammer to be specific the VERB NOUN ADJECTIVE points will be according to that
# After we will calculate average of the point and return the points 

test = "since if we are directly given text input  there will be more sentence bu if we are using output of "

import types
import nltk
import nltk.corpus 
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize
from nltk.data import load
from nltk.corpus import conll2000
from nltk.tree import Tree
from nltk import conlltags2tree, tree2conlltags
from nltk import pos_tag, ne_chunk

# We have to make diffrent function for this download becuase we don't need this every time (According to my observation)
nltk.download('averaged_perceptron_tagger')
nltk.download('conll2000')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def checkGrammer(studentAnswer):
    # Here we are tokenizing into sentences 
    fileDocument = []
    answer = studentAnswer
    TokenizeAnswer = sent_tokenize(answer)
    for token in TokenizeAnswer:
        fileDocument.append(token)
    # print(fileDocument)
    sentencesLenght = len(fileDocument)
   
    # since if we are directly given text input  there will be more sentence bu if we are using output of 
    # voice the text is complet one single string ie no fullstop commas 
    # Becuase of above reason i am using While loop to check each sentence if possible.
    sentence = 0
    while sentence < sentencesLenght:
        
        # Word Tokenize sentence
        word_tokens = word_tokenize(fileDocument[sentence])
        # print(word_tokens)   
        sentence += 1
        
        # Tagging the grammer tag to words like Verb noun
        pre_chunk = nltk.pos_tag(word_tokens)
        # print(pre_chunk)
        tree = ne_chunk(pre_chunk)
        # Now we have to add out own rule to fillter out
        grammer_np = ("NP: {<DT>?<JJ>*<NN>}")
        chunk_parser = nltk.RegexpParser(grammer_np)
        chunk_result = chunk_parser.parse(tree)
        for tr in chunk_result:
            tr1 = str(tr)
            s1 = Tree.fromstring(tr1)
            s2 = s1.productions()
        #print(type(s2))
        #chunk_tree =  Tree.fromstring("(S (NP I) (VP (V saw) (NP him)))")
        # chunl_treet = conll2000.chunked_sents(test, chunk_types=['NP'])
        # test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
        # print(type(test_sents))
        # print(chunk_parser.evaluate(test_sents))
        # print(test_sents)
        # chunk_parser.evaluate(chunk_result)
        # print(type(chunk_result))
        # print(len(chunk_result))
        #print(chunk_result)
        # iob_tags = tree2conlltags(chunk_result)
        # print(iob_tags)
        #print(nltk.chunk.conllstr2tree(iob_tags, chunk_types=['NP']))  
        # cp = nltk.RegexpParser("")
       # test_sents = conll2000.chunked_sents(iob_tags, chunk_types=['NP'])
        #print(test_sents)
        # print(cp.evaluate(chunk_result))


        # evaluating grammer 
        # cp = nltk.RegexpParser("")
        # grammar = r"NP: {<[CDJNP].*>+}"
        # cp = nltk.RegexpParser(grammar)
        # print(cp.evaluate(test))



# checkGrammer(test)    

