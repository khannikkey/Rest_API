from django.contrib import admin
from testapp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display= ['id', 'eno', 'esal', 'ename', 'eaddr']

admin.site.register(Employee, EmployeeAdmin)
