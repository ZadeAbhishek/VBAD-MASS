from django.contrib import admin

# Register your models here.
from .models import  student, studentID,teacher,noTest

admin.site.register(student)
admin.site.register(teacher)
admin.site.register(studentID)
admin.site.register(noTest)
