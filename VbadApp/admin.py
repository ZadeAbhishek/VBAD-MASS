from django.contrib import admin

# Register your models here.
from .models import  student, studentID,teacher,question,result,Testno

admin.site.register(student)
admin.site.register(teacher)
admin.site.register(studentID)
admin.site.register(question)
admin.site.register(result)
admin.site.register(Testno)

