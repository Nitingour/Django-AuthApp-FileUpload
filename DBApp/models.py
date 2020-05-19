from django.db import models

# Create your models here.

# Table : name,no. and names of column,data type ,size
department=(('sales','SALES'),('purchase','PURCHASE'),('account','ACCOUNT'))

class Employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=60)
    salary=models.FloatField()
    address=models.CharField(max_length=100)
    department=models.CharField(max_length=40,choices=department,default='')

#from datetime import datetime
class Upload(models.Model):
    name=models.CharField(max_length=50)
    pic=models.FileField(upload_to='images/')
    author=models.CharField(max_length=50)
    upload_date=models.DateTimeField(auto_now_add=True)












#
