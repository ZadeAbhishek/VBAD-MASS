from tkinter import CASCADE
from django.db import models

from VbadApp.pyFile.model import model

# Create your models here.
class Testno(models.Model):
    testno = models.IntegerField(default = 0)
    TestName = models.CharField(max_length=100)

class teacher(models.Model):
     teacherNumber = models.IntegerField(default = 0) 
     teacherName = models.CharField(max_length=100)
     subjectName = models.CharField(max_length=100)
     testno = models.ForeignKey(Testno,on_delete=models.CASCADE)

class question(models.Model):
    question = models.CharField(max_length=1000)
    answer = models.TextField()
    keyword = models.CharField(max_length=1000)
    testno = models.ForeignKey(Testno,on_delete=models.CASCADE)
    teacherNumber = models.ForeignKey(teacher,on_delete=models.CASCADE)

class student(models.Model):
    studentName = models.CharField(max_length=1000)

class result(models.Model):
    resultid = models.AutoField
    studentname = models.ForeignKey(student,on_delete=models.CASCADE)
    testno = models.ForeignKey(Testno,on_delete=models.CASCADE)
    teacherNumber = models.ForeignKey(teacher,on_delete=models.CASCADE)
    questionNumber = models.CharField(max_length=50)
    tdifdSimilarity = models.CharField(max_length=50)
    vectorSimilarity = models.CharField(max_length=50)
    keywordSimilarity = models.CharField(max_length=50)
    GrammerSimilarity = models.CharField(max_length=50)
    finalResult = models.CharField(max_length=10)


class studentID(models.Model):
    studentid = models.AutoField
    questionNumber = models.CharField(max_length=50)
    tdifdSimilarity = models.CharField(max_length=50)
    vectorSimilarity = models.CharField(max_length=50)
    keywordSimilarity = models.CharField(max_length=50)
    GrammerSimilarity = models.CharField(max_length=50)
    finalResult = models.CharField(max_length=10)


   