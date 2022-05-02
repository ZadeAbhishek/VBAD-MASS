from django.contrib import admin

# Register your models here.
from .models import  Questions, StudentResult, Students, Teachers,Answer


admin.site.register(Students)
admin.site.register(Teachers)
admin.site.register(StudentResult)
admin.site.register(Questions)
admin.site.register(Answer)

