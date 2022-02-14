from django import forms

class questionForm(forms.Form):
    questionNumber = forms.IntegerField()
    question = forms.CharField()
    answer = forms.CharField()
    keyword = forms.CharField()
    testNo = forms.IntegerField() 
    
class testnum(forms.Form):
    testNo = forms.IntegerField()    