from django.contrib import admin

# Register your models here.
from DBApp.models import Employee,Upload


class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eid','ename','salary','address','department']

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Upload)
