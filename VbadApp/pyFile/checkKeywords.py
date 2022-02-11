## In this folder we extracting the keyword using gensim model anlos we are comparing
from difflib import SequenceMatcher
from rake_nltk import Rake
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer



# here test = Student Answer 
# testKeywords = teachers Keywords 

# Function to check keywords
def checkKeyword(test,testKeywords):

   #print("..........................Extracting keyowords...................................")
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
   #print(keyword_extracted)
   testKeywords = word_tokenize(testKeywords)
   #print(testKeywords)
   # Getting lenght
   testKeywordslen = len(testKeywords)


  # Now idea is to comare each word of teachers keyowrd woth student each keyword
  # comparing words gives us ratio 
  # get the avarage ratio (may over answer)

   def compare(Studentkeyword,teacherkeyword):
      average = 0
      elemfound = []
      for twords in range(len(teacherkeyword)) :
          for swords in range(len(Studentkeyword)):
              if (SequenceMatcher(None,teacherkeyword[twords],Studentkeyword[swords]).ratio()) > 0.95:
                 elemfound.append(Studentkeyword[swords])
                 print(elemfound)
                 #print('Found : {}'.format(Studentkeyword[swords]))
                 average += 1
      elemfound = list(dict.fromkeys(elemfound))
      #print(elemfound)
      elemfound = len(elemfound)
      #print(elemfound)
      #print(average) 
      #print(elemfound)
      #print(testKeywordslen)
      if(elemfound == 0):
         return 0
      if(elemfound == testKeywordslen):
         return 100
      return ((elemfound)/(average))*100

   count = compare(keyword_extracted,testKeywords)
   #print(count)
   return count



###### Unit test for This folder  ########


test3 = """Git is very fast and scalable compared to other version control systems.
The fetching power from a local repository is much faster than what possible with remote server.
Data Assurance
 The Git history is stored in such a way that the ID of a particular version depends upon the complete development history leading up to that commit.
Once published, it is not possible to change the old versions without it being noticed.
Automatic Garbage Collection
 Git automatically performs garbage collection when enough loose objects have been created in the repository.
Garbage collection can be called explicitly using git gc –prune.
Periodic explicit object packing
 Git stores each newly created object as a separate file. It uses packs that store a large number of objects in a single file (or network byte stream) called packfile, delta-compressed among themselves.
A corresponding index file is created for each pack file, specifying the offset of each object in the packfile.
The process of packing can be very expensive computationally.
Git allows the expensive pack operation to be deferred until later when time does not matter.
Git does periodic repacking automatically but manual repacking can be done with the git gc command.
How GIT Works"""
test5 = 'git fast scalable compared version control system facing power local repository much faster possible remote server data assurance git history stored way particular version depends upon complete development history leading automation garbage collection get automatically performs garbage collection enough loses object created repository periodic explain packaged stories new create object separate file packet discover data large number object stream file called packet file'

#test = "git pull command fetch remote repository Merge remote upstream"
testKeywords = "git pull command fetch remote repository Merge upstream"

#checkKeyword(test5,testKeywords)