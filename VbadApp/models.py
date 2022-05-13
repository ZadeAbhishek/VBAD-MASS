from tkinter import CASCADE
from django.db import models

from VbadApp.pyFile.model import model

# Create your models here.

class Teachers(models.Model):
     teacherName = models.CharField(max_length=100)
     testno = models.IntegerField(default = 0)
     TestName = models.CharField(max_length=100)
     

     def  __str__(self):
         return self.teacherName


class Students(models.Model):
    studentName = models.CharField(max_length=500)

    def  __str__(self):
         return str(self.studentName)

class Questions(models.Model):
    Teacher = models.ForeignKey(Teachers,on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    Answer = models.TextField()
    keyword = models.CharField(max_length=1000)

    def  __str__(self):
         return self.question


class Answer(models.Model):
    studentname = models.ForeignKey(Students,on_delete=models.CASCADE)
    question = models.ForeignKey(Questions,on_delete=models.CASCADE)
    answer = models.TextField()

    def  __str__(self):
         return self.answer   

def No_name():
    return "No name"

class StudentResult(models.Model):
    studentname = models.ForeignKey(Students,on_delete=models.CASCADE,verbose_name="Studentname",null=True, default=No_name)
    questionNumber = models.CharField(max_length=50)
    question = models.TextField()
    TeacherAnswer = models.TextField()
    answer = models.TextField()
    tdifdSimilarity = models.CharField(max_length=50)
    vectorSimilarity = models.CharField(max_length=50)
    keywordSimilarity = models.CharField(max_length=50)
    GrammerSimilarity = models.CharField(max_length=50)
    finalResult = models.CharField(max_length=10)
    total = models.CharField(max_length=50)

    def  __str__(self):
         return str(self.studentname)

class notice(models.Model):
    topic = models.CharField(max_length=50)
    notice = models.TextField()


    def  __str__(self):
         return str(self.topic)

   