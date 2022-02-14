from tkinter import CASCADE
from django.db import models

from VbadApp.pyFile.model import model

# Create your models here.
class noTest(models.Model):
    testno = models.IntegerField(default = 0) 

class student(models.Model):
    student_id = models.AutoField
    testNumber= models.SmallIntegerField()
    questionNumber = models.CharField(max_length=1000)

class teacher(models.Model):
    teacher_id = models.AutoField
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=1000)
    keyword = models.CharField(max_length=1000)
    questionNo = models.IntegerField(default = 0)
    referring_testno = models.IntegerField(default = 0)


class studentID(models.Model):
    studentid = models.AutoField
    questionNumber = models.CharField(max_length=50)
    tdifdSimilarity = models.CharField(max_length=50)
    vectorSimilarity = models.CharField(max_length=50)
    keywordSimilarity = models.CharField(max_length=50)
    GrammerSimilarity = models.CharField(max_length=50)
    finalResult = models.CharField(max_length=10)


   