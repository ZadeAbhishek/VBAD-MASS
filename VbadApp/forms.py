from django import forms

class questionForm(forms.Form):
    question = forms.CharField(widget=forms.Textarea)
    answer = forms.CharField(widget=forms.Textarea)
    keyword = forms.CharField()
    testNo = forms.IntegerField()
    teacherNo = forms.IntegerField()  
    
class testnum(forms.Form):
    testNo = forms.IntegerField()
    testname = forms.CharField()    