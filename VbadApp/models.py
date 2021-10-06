from django.db import models

# Create your models here.
class studentID(models.Model):
    studentid = models.AutoField
    questionNumber = models.CharField(max_length=50)
    tdifdSimilarity = models.CharField(max_length=50)
    vectorSimilarity = models.CharField(max_length=50)
    keywordSimilarity = models.CharField(max_length=50)
    GrammerSimilarity = models.CharField(max_length=50)
    finalResult = models.CharField(max_length=10)
    
