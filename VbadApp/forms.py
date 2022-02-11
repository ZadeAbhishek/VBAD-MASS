from django import forms

class questionForm(forms.Form):
    questionNumber = forms.IntegerField()
    question = forms.CharField()
    answer = forms.CharField()
    keyword = forms.CharField()
    