from django.contrib import admin
from .models import Department,Student

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display =['name','age','department','level','status','date_created']



admin.site.register(Department)
admin.site.register(Student,StudentAdmin)


