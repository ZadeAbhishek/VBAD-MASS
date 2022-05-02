## This folder is to check the similarity betwen the the teacher and student answer code works not upto point
# need corrections
# Some of the variable is mismatch here will work on this 
import nltk 
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import gensim
import numpy as np 
from nltk.corpus import stopwords 

# genism help to create bag of word
def checkparaSimilarity(studentAnswer, teacherAnswer):
    fileDocument = []
    answer = studentAnswer
    TokenizeAnswer = sent_tokenize(answer)
    for token in TokenizeAnswer:
        fileDocument.append(token)
   # print(fileDocument)


    word_tokenizer = [[w.lower() for w in word_tokenize(text)] for text in fileDocument]
    print(".............Checking Similarity.............")
    # print(word_tokenizer)

    # creating bag of words with unique id to compare and also it frequnecy of occur
    dictionary = gensim.corpora.Dictionary(word_tokenizer)
    corpus = [dictionary.doc2bow(word_tokens) for word_tokens in word_tokenizer]

    # term frequency and inverse document frequency this will help to take out important works i.e 
    # words that occurs more time 
    tf_idf = gensim.models.TfidfModel(corpus)
    sameMeter = []
    similarity = gensim.similarities.Similarity('./tf_similarity',tf_idf[corpus], num_features=len(dictionary))



     ## repeating everythng for comparing  

    fileDocument2 = []
    teacheranswer = teacherAnswer
    TokenizeTeacherAnswer = sent_tokenize(teacheranswer)
    for token in TokenizeTeacherAnswer:
        fileDocument2.append(token)
    # print(fileDocument2)

    for line in fileDocument2:
      teaher_word_tokenizer = [w.lower() for w in word_tokenize(line)]
     # print(teaher_word_tokenizer)
      teacher_word_bow = dictionary.doc2bow(teaher_word_tokenizer)


    teacher_word_tf = tf_idf[teacher_word_bow]
    sum_of_similarity = (np.sum(similarity[teacher_word_tf], dtype=np.float32))
    #print(sum_of_similarity)
    #print(len(fileDocument))
    percetage_similairty = round(float((sum_of_similarity / len(fileDocument))* 100))
    print('percentage: {}'.format(percetage_similairty))
    return percetage_similairty


def similarity(teacher,student):
        X_list = word_tokenize(teacher)  
        Y_list = word_tokenize(student)
        sw = stopwords.words('english')  
        l1 =[];l2 =[]
        X_set = {w for w in X_list if not w in sw}  
        Y_set = {w for w in Y_list if not w in sw} 
    
        rvector = X_set.union(Y_set)  
        for w in rvector: 
          if w in X_set: l1.append(1)
          else: l1.append(0) 
          if w in Y_set: l2.append(1) 
          else: l2.append(0) 
        c = 0
    
        for i in range(len(rvector)): 
          c+= l1[i]*l2[i] 
        cosine = c / float((sum(l1)*sum(l2))**0.5) 
        # print("similarity: ", cosine * 100)
        return cosine * 100








## Unit test for this function

test = """Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.
Git relies on the basis of distributed development of a software where more than one developer may have access to the source code of a specific application and can modify changes to it which may be seen by other developers..
Initially designed and developed by Linus Torvalds for Linux kernel development in 2005.
Every git working directory is a full-fledged repository with complete history and full version-tracking capabilities, independent of network access or a central server.
Git allows a team of people to work together, all using the same files. And it helps the team cope up with the confusion that tends to happen when multiple people are editing the same files.
Why Use Version Control Software?
Version control software allows the user to have “versions” of a project, which show the changes that were made to the code over time, and allows the user to backtrack if necessary and undo those changes.
This ability alone – of being able to compare two versions or reverse changes, makes it fairly invaluable when working on larger projects.
In a version control system, the changes would be saved just in time – a patch file that could be applied to one version, in order to make it the same as the next version.
All versions are stored on a central server, and individual developers checkout and upload changes back to this server.
 Characteristics of Git

Strong support for non-linear development
Git supports rapid branching and merging, and includes specific tools for visualizing and navigating a non-linear development history.
A major assumption in Git is that a change will be merged more often than it is written.
Branches in Git are very lightweight.
Distributed development
 Git provides each developer a local copy of the entire development history, and changes are copied from one such repository to another.
The changes can be merged in the same way as a locally developed branch very efficiently and effectively.
Compatibility with existing systems/protocol
 Git has a CVS server emulation, which enables the use of existing CVS clients and IDE plugins to access Git repositories.
    4.  Efficient handling of large projects



 Git is very fast and scalable compared to other version control systems.
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
How GIT Works

A Git repository is a key-value object store where all objects are indexed by their SHA-1 hash value.
All commits, files, tags and filesystem tree nodes are different types of objects living in this repository.
A Git repository is a large hash table with no provision made for hash collisions.
Git specifically works by taking “snapshots” of files" """

test2 = """ METHOD 3 (A Juggling Algorithm) 
This is an extension of method 2. Instead of moving one by one, divide the array in different sets 
where number of sets is equal to GCD of n and d and move the elements within sets. 
If GCD is 1 as is for the above example array (n = 7 and d =2), then elements will be moved within one set only, we just start with temp = arr[0] and keep moving arr[I+d] to arr[I] and finally store temp at the right place.
Here is an example for n =12 and d = 3. GCD is 3 and """ 


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

teachetTestAnswer = "The git pull command is used to fetch and download content from a remote repository and immediately update the local repository to match that content. Merging remote upstream changes into your local repository is a common task in Git-based collaboration work flows. The git pull command is actually a combination of two other commands, git fetch followed by git merge. In the first stage of operation git pull will execute a git fetch scoped to the local branch that HEAD is pointed at. Once the content is downloaded, git pull will enter a merge workflow. A new merge commit will be-created and HEAD updated to point at the new commit."
test4 = "algorithm is a finite set of instructions that I followed accomplished a particular algorithm must satisfy the following criteria input zero for more quality rx10 be supplied output at least one qualities for seed definition if each instruction is clear and ambitious fitness if stress out the construction of an algorithm that all cases the algorithm terminate after the Infinity of step very every instruction must be very busy so that it can be carried out in the principal by the person using one pencil and the paper is not enough that each operation must be defined as a Priority write three it also must be visible ."

#checkparaSimilarity(teachetTestAnswer,teachetTestAnswer)
#similarity(teachetTestAnswer,teachetTestAnswer)