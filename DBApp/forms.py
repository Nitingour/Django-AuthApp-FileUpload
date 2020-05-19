
from django import forms
from .models import Employee,Upload

from django.contrib.auth.models import User
# class EmployeeForm(forms.Form):
#     eid=forms.IntegerField()
#     ename=forms.CharField()
#     salary=forms.FloatField()
#     address=forms.CharField()
#     department=forms.CharField()

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__' # include all field in form
        #fields=('eid','ename','salary')  #includes perticular fields
        #exclude=['salary'] #exclude perticular field
        widgets={'address':forms.Textarea(attrs={'rows':3,'cols':30})}

class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        #fields='__all__'
        fields=('username','password','email','first_name','last_name')
        widgets={'password':forms.PasswordInput()}

class UploadForm(forms.ModelForm):
    class Meta:
        model=Upload
        fields=('name','pic')
        






#
