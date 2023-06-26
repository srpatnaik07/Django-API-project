from django.contrib import admin
from college.models import Notice,Student

# Register your models here.
@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['id','subject','msg','cr_date']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','address']
