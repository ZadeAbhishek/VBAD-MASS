from gingerit.gingerit import GingerIt
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 



averageScore = 0
sentencesLenght = 0
def checkGrammer(studentAnswer):
    # Here we are tokenizing into sentences 
    fileDocument = []
    answer = studentAnswer
    TokenizeAnswer = sent_tokenize(answer)
    for token in TokenizeAnswer:
        fileDocument.append(token)
    # print(fileDocument)
    global sentencesLenght 
    sentencesLenght = len(fileDocument)
    lines = 0
    refineDocument = []
    while lines < sentencesLenght:
        # print('.............Checking Lines :{}.....................'.format(lines))
        if(len(fileDocument[lines]) > 100):
            start = 0
            end = 100
            spt = True
            while(spt):
               #print('.............Checking from line :{}.....................'.format(start))
               #print(start)
               refineDocument.append(split(fileDocument[lines],start,end))
               if(start > len(fileDocument[lines])):
                   spt = False
                   end = len(fileDocument[lines])
               else:
                   start += 100
                   end += 100    
        else:
            refineDocument.append(fileDocument[lines])
        lines += 1         
    # since if we are directly given text input  there will be more sentence bu if we are using output of 
    # voice the text is complet one single string ie no fullstop commas 
    # Becuase of above reason i am using While loop to check each sentence if possible.
    sentence = 0
    while sentence < len(refineDocument):
        
        # print(word_tokens)
        parser = GingerIt()
        #print('Sentence lenght {}'.format(len(refineDocument[sentence])))
        cG = parser.parse(refineDocument[sentence])
        ginger_corrections = cG['corrections']
        #print('correctionlenght{}'.format(len(ginger_corrections)))
        #print(cG["result"])
        global averageScore
        averageScore += len(ginger_corrections)
        sentence += 1 
        # X_list = word_tokenize(fileDocument[sentence])  
        # Y_list = word_tokenize(cG["result"])
        # sw = stopwords.words('english')  
        # l1 =[];l2 =[]
        # X_set = {w for w in X_list if not w in sw}  
        # Y_set = {w for w in Y_list if not w in sw} 
    
        # rvector = X_set.union(Y_set)  
        # for w in rvector: 
        #   if w in X_set: l1.append(1)
        #   else: l1.append(0) 
        #   if w in Y_set: l2.append(1) 
        #   else: l2.append(0) 
        # c = 0
    
        # for i in range(len(rvector)): 
        #   c+= l1[i]*l2[i] 
        # cosine = c / float((sum(l1)*sum(l2))**0.5) 
        # #print("similarity: ", cosine)
        # global averageScore 
        # averageScore += cosine    
        # sentence += 1
    total = (averageScore/len(refineDocument)) * 10
    total = 100 - total
    total = round(total, 2)
    #print(total)
    return total

def split(string,startposition,end):
    splt = ''
    #print('lenght of send string {}'.format(len(string)))
    #print(startposition,end)
    while(startposition >= (end)):
        #print(startposition)
        splt +=  string[startposition]
        #print('lenghr of string {}'.format(len(splt)))
        startposition += startposition
    return splt


# unit test
text = ''' was delighted to read you're letter last week. Its always a pleasure to recieve the latest news and to here that you and your family had a great summer. We spent last week at the beach and had so much fun on the sand and in the water exploring the coast we weren't prepared for the rains that came at the end of the vacation. The best parts of the trip was the opportunities to sightsee and relax. My kids are back in school to. I find their are less things to worry about now that the kids are at school all day. There is plenty of fun things to do in the summer, but by August, I've running out of ideas. I've excepted the fact that we'll have to think up brand new activities next summer; hoping to round up some creative ideas soon.'''
text2 = 'was delighted to read youre letter last week Its always a pleasure. to recieve the latest news and to here that you and your family had a great summer We spent last week at the beach and had so much fun on the sand and in the water exploring the coast we werent prepared for the rains that came at the end of the vacation The best parts of the trip was the opportunities to sightsee and relax My kids are back in school to I find their are less things to worry about now that the kids are at school all day There is plenty of fun things to do in the summer but by August Ive running out of ideas Ive excepted the fact that well have to think up brand new activities next summer hoping to round up some creative ideas soon'
text3 = 'program call subroutine approach mein application order flow write stack underflow decrement vector written function element peace control return algorithm solved part every recursion determine base case combination base suitable recursion recursion recursion solution accept time time space'
#checkGrammer(text2)        