## In this folder we extracting the keyword using gensim model anlos we are comparing
from difflib import SequenceMatcher
from rake_nltk import Rake
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer


test = "The git pull command is used to fetch and download content from a remote repository and "
testKeywords = "git pull command fetch remote repository Merge remote upstream commit"
 
# here test = Student Answer 
# testKeywords = teachers Keywords 

# Function to check keywords
def checkKeyword(test,testKeywords):

   print("..........................Extracting keyowrds...................................")
   testKeywords = testKeywords.lower()
   test = test.lower()
   # This will reduce the lines for example the if there is 10 line 
   # Upto know keyword extraction is done know we have to to compare
   # my idea is to use Rake from nltk which strongest word for nlp
   rake_nltk_var = Rake()
   rake_nltk_var.extract_keywords_from_text(test)
   keyword_extracted = rake_nltk_var.get_ranked_phrases()


   # Detokenizing tests Answers (becuase this keywords are combine with other keywords)
   keyword_extracted = TreebankWordDetokenizer().detokenize(keyword_extracted)
   # Complete seperating and tokenizing the key word
   keyword_extracted = word_tokenize(keyword_extracted)
   print(keyword_extracted)
   testKeywords = word_tokenize(testKeywords)
   print(testKeywords)
   # Getting lenght
   testKeywordslen = len(testKeywords)


  # Now idea is to comare each word of teachers keyowrd woth student each keyword
  # comparing words gives us ratio 
  # get the avarage ratio (may over answer)

   def compare(Studentkeyword,teacherkeyword):
      average = 0
      for twords in range(len(teacherkeyword)) :
          for swords in range(len(Studentkeyword)):
              if (SequenceMatcher(None,teacherkeyword[twords],Studentkeyword[swords]).ratio()) > 0.8: 
                 average += 1
      return average

   count = compare(keyword_extracted,testKeywords)
   count = (count/testKeywordslen)*100 
   print(count)

checkKeyword(test,testKeywords)