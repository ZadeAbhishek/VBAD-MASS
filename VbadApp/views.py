from email import charset
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import QueryDict
# Create your views here.
# from django.http.response import HttpResponse
from django.shortcuts import render

from VbadApp.models import StudentResult,Teachers,Questions,Students,Teachers,Answer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .pyFile.init import checkinit 
from django.core.paginator import Paginator
# from .forms import questionForm,testnum
studNamedb = ""
studentname = ''
# Create your views here.
@csrf_exempt
def index(request,id,msg):
    print(studentname)
    # So i am thinking of calling the 
    NameStudent = request.POST.get('studentname')
    question = request.POST.get('question')
    answer = request.POST.get('answer')
    teacherAnswer = request.POST.get('teacherAnswer')
    teacherKeyword = request.POST.get('teacherKeyword')
    questionNumber = request.POST.get('questionNumber')
    
    print( NameStudent,question,answer,teacherAnswer,teacherKeyword,questionNumber)
    
    # teacherAnswerone = "A VCS keeps track of the contributions of the developers working as a team on the projects. They maintain the history of code changes done and with project evolution, it gives an upper hand to the developers to introduce new code, fix bugs, and run tests with confidence that their previously working copy could be restored at any moment in case things go wrong."
    # teacherKeyword = "fix bugs run tests"
    
    #sr = StudentResult(studentname=str(NameStudent),questionNumber=str(1),tdifdSimilarity =str(similarAnswer),vectorSimilarity = str(similarit),keywordSimilarity=str(keyWordtest),GrammerSimilarity = str(GrammerScore),finalResult=finalresult)
    
    # secondAnswer = request.POST.get('answertwo')
    # teacherAnswertwo = "The git pull command is used to fetch and download content from a remote repository and immediately update the local repository to match that content. Merging remote upstream changes into your local repository is a common task in Git-based collaboration work flows. The git pull command is actually a combination of two other commands, git fetch followed by git merge. In the first stage of operation git pull will execute a git fetch scoped to the local branch that HEAD is pointed at. Once the content is downloaded, git pull will enter a merge workflow. A new merge commit will be-created and HEAD updated to point at the new commit."
    # teacherKeywordtwo = "pull fetch Merge"
    # similarAnswer, similarit, keyWordtest, GrammerScore, finalresult = checkinit(str(secondAnswer),teacherAnswertwo,teacherKeywordtwo)
    # formstwo = StudentResult(questionNumber=str(2),tdifdSimilarity =str(similarAnswer),vectorSimilarity = str(similarit),keywordSimilarity=str(keyWordtest),GrammerSimilarity = str(GrammerScore),finalResult=finalresult)
    
    # thirdAnswer = request.POST.get('answerthree')
    # teacherAnswerthree = "Git usually handles feature merges automatically but sometimes while working in a team environment, there might be cases of conflicts such as When two separate branches have changes to the same line in a file.A file is deleted in one branch but has been modified in the other.These conflicts have to be solved manually after discussion with the team as git will not be able to predict what and whose changes have to be given precedence."
    # teacherKeywordthree = "separate branches manually"
    # similarAnswer, similarit, keyWordtest, GrammerScore, finalresult = checkinit(str(thirdAnswer),teacherAnswerthree,teacherKeywordthree)
    # formsthree = StudentResult(questionNumber=str(3),tdifdSimilarity =str(similarAnswer),vectorSimilarity = str(similarit),keywordSimilarity=str(keyWordtest),GrammerSimilarity = str(GrammerScore),finalResult=finalresult)
    
    
    # data = {}
    # if is_ajax(request=request):
    #     formsone.save()
    #     formstwo.save()
    #     formsthree.save()
    #    # data['StudentResult'] = forms.clean_data.get('StudentResult')
    #    # data['status'] = 'ok'
    #     return JsonResponse(data)
    # context = {
    #     'formsone': formsone,
    #     'formstwo': formstwo,
    #     'formsthree': formsthree,
    # } 

    teachername = Teachers.objects.get(id=id).id
    print(teachername)
    questions = Questions.objects.filter(Teacher = teachername).values()
    paginator = Paginator(questions,1)
    page_num=request.GET.get('page',1)
    questions = paginator.page(page_num)
    similarAnswer, similarit, keyWordtest, GrammerScore, finalresult = checkinit(str(answer),str(teacherAnswer),str(teacherKeyword))
    # studname = Students(studentName=str(NameStudent))
    # studentinstance = Students()
    # studentinstance.studentName = msg
    result = StudentResult(TeacherAnswer=str(teacherAnswer),question=str(question),answer=str(answer),studentname=Students.objects.get(studentName=msg),questionNumber=str(questionNumber),tdifdSimilarity =str(similarAnswer),vectorSimilarity = str(similarit),keywordSimilarity=str(keyWordtest),GrammerSimilarity = str(GrammerScore),finalResult=finalresult)
    data = {}
    if is_ajax(request=request):
        result.save()
        # return JsonResponse(data)
    return render(request,'index.html',{'quest':questions})

# def about(request):
#     return HttpResponse("This is about")
@csrf_exempt
def home(request) :
    

    return render(request,'main.html')

def result(request) :
    CompleteResult = Students.objects.all
    return render(request,'result.html',{'allresult':CompleteResult})

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' 

@csrf_exempt
def questionpanel(request):
    # form = questionForm(request.POST)
    # testnoobj = Testno.objects.all
    # if form.is_valid():
    #     context = {}
    #     Tquestion = form.cleaned_data['question']
    #     Tanswers = form.cleaned_data['answer']
    #     Tkeywords = form.cleaned_data['keyword']
    #     Tnumber = form.cleaned_data['teacherNo']
    #     testNo = form.cleaned_data['testNo']
    #     # testreference = Testno.objects.filter(testno=testNo)
    #     print(Testno.objects.all)
    #     testreference = Testno(testno=testNo)
    #     testreference.save()
    #     TeacherNumber = teacher(teacherNumber=Tnumber,testno=testreference)
    #     TeacherNumber.save()
    #     print(Testno.objects.all)
    #     #notestdb = noTest.objects.get()
    #     teacherdb = question(question=Tquestion,answer=Tanswers,keyword=Tkeywords,testno=testreference,teacherNumber=TeacherNumber)
    #     #    testno=testreference,teacherNumber=Tnumber
    #     #teacherdb.referring_testno_id = testNo
    #     print(testNo)
    #     teacherdb.save()
    #     #notestdb.save()
    return render(request,'questionpanel.html')

def testno(request,msg):
    name = msg
    studentinstance = Students()
    studentinstance.studentName = msg
    studentinstance.save()
    teacherDetail = Teachers.objects.all().order_by('id')
    
    return render(request,'testno.html',{'Teacherdetails':teacherDetail,'studname':name})

def studentResult(request,id):
    # StudentRestDetail = StudentResult.objects.get(studentname=id)
    # studname = str(msg)
    vectorSimilarity = 0
    tdfidfSimilarity = 0.0
    KeywordFound = 0.0
    GrammerCheck = 0

    Student = Students.objects.get(id=id).id
    studentName = Students.objects.filter(studentName = id)
    StudentRestDetail = StudentResult.objects.filter(studentname = Student).values()
    for sr in StudentRestDetail:
        #print("tdifdSimilarity:",sr['tdifdSimilarity'])
        tdfidfSimilarity = tdfidfSimilarity + int(sr['tdifdSimilarity'])
        #print("tdifdSimilarity:",tdfidfSimilarity)
        #print("vectorSimilarity:",sr['vectorSimilarity'])
        vectorSimilarity = vectorSimilarity + float(sr['vectorSimilarity'])
        #print("vectorSimilarity:",vectorSimilarity)
        #print("keywordSimilarity:",sr['keywordSimilarity'])
        KeywordFound = KeywordFound + float(sr['keywordSimilarity'])
        #print("keywordSimilarity:",KeywordFound)
        #print("GrammerSimilarity",sr['GrammerSimilarity'])
        GrammerCheck = GrammerCheck + int(sr['GrammerSimilarity'])
        #print("GrammerSimilarity",GrammerCheck)


        tdfidfSimilarity = int(tdfidfSimilarity)
        vectorSimilarity= int(vectorSimilarity)
        KeywordFound = int(KeywordFound)
        GrammerCheck = int(GrammerCheck)

        tdfidfSimilarity = int(20 * (tdfidfSimilarity/100))
        vectorSimilarity = int(30 * (vectorSimilarity/100))
        KeywordFound = int(30 * (KeywordFound/100))
        GrammerCheck = int(20 * (GrammerCheck/100))
  
        total = tdfidfSimilarity + vectorSimilarity + KeywordFound + GrammerCheck
    print("tdifdSimilarity:",tdfidfSimilarity)
    print("vectorSimilarity:",vectorSimilarity)
    print("keywordSimilarity:",KeywordFound)
    print("GrammerSimilarity",GrammerCheck)
    print("total",total)      
    return render(request,'studentResult.html',{'studentResult':StudentRestDetail}) 


def createTest(request):
    # testform = testnum(request.POST)
    # if testform.is_valid():
    #     create_test = testform.cleaned_data['testNo']
    #     create_name = testform.cleaned_data['testname']
    #     testdb = Testno(testno=create_test,TestName = create_name)
    #     testdb.save()
    return render(request,'createtest.html',{'testform': testform})


   