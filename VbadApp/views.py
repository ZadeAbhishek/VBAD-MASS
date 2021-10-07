from django.shortcuts import render
from django.http import QueryDict
# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render

from VbadApp.models import studentID
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .pyFile.init import checkinit 

# Create your views here.
@csrf_exempt
def index(request):

    # So i am thinking of calling the 
    NameStudent = request.POST.get('studentname')
    fristAnswer = request.POST.get('answerone')
    teacherAnswerone = "A VCS keeps track of the contributions of the developers working as a team on the projects. They maintain the history of code changes done and with project evolution, it gives an upper hand to the developers to introduce new code, fix bugs, and run tests with confidence that their previously working copy could be restored at any moment in case things go wrong."
    teacherKeyword = "fix bugs run tests"
    similarAnswer, similarit, keyWordtest, GrammerScore, finalresult = checkinit(str(fristAnswer),teacherAnswerone,teacherKeyword)
    formsone = studentID(questionNumber=str(1),tdifdSimilarity =str(similarAnswer),vectorSimilarity = str(similarit),keywordSimilarity=str(keyWordtest),GrammerSimilarity = str(GrammerScore),finalResult=finalresult)
    
    secondAnswer = request.POST.get('answertwo')
    teacherAnswertwo = "The git pull command is used to fetch and download content from a remote repository and immediately update the local repository to match that content. Merging remote upstream changes into your local repository is a common task in Git-based collaboration work flows. The git pull command is actually a combination of two other commands, git fetch followed by git merge. In the first stage of operation git pull will execute a git fetch scoped to the local branch that HEAD is pointed at. Once the content is downloaded, git pull will enter a merge workflow. A new merge commit will be-created and HEAD updated to point at the new commit."
    teacherKeywordtwo = "pull fetch Merge"
    similarAnswer, similarit, keyWordtest, GrammerScore, finalresult = checkinit(str(secondAnswer),teacherAnswertwo,teacherKeywordtwo)
    formstwo = studentID(questionNumber=str(2),tdifdSimilarity =str(similarAnswer),vectorSimilarity = str(similarit),keywordSimilarity=str(keyWordtest),GrammerSimilarity = str(GrammerScore),finalResult=finalresult)
    
    thirdAnswer = request.POST.get('answerthree')
    teacherAnswerthree = "Git usually handles feature merges automatically but sometimes while working in a team environment, there might be cases of conflicts such as When two separate branches have changes to the same line in a file.A file is deleted in one branch but has been modified in the other.These conflicts have to be solved manually after discussion with the team as git will not be able to predict what and whose changes have to be given precedence."
    teacherKeywordthree = "separate branches manually"
    similarAnswer, similarit, keyWordtest, GrammerScore, finalresult = checkinit(str(thirdAnswer),teacherAnswerthree,teacherKeywordthree)
    formsthree = studentID(questionNumber=str(3),tdifdSimilarity =str(similarAnswer),vectorSimilarity = str(similarit),keywordSimilarity=str(keyWordtest),GrammerSimilarity = str(GrammerScore),finalResult=finalresult)
    
    
    data = {}
    if request.is_ajax():
        formsone.save()
        formstwo.save()
        formsthree.save()
       # data['studentid'] = forms.clean_data.get('studentid')
       # data['status'] = 'ok'
        return JsonResponse(data)
    context = {
        'formsone': formsone,
        'formstwo': formstwo,
        'formsthree': formsthree,
    } 
    return render(request,'index.html',context)

def about(request):
    return HttpResponse("This is about")

def home(request) :
    return render(request,'main.html')

def result(request) :
    CompleteResult = studentID.objects.all
    return render(request,'result.html',{'allresult':CompleteResult})