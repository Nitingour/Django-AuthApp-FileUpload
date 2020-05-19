from django.shortcuts import render

# Create your views here.
from DBApp.models import Employee,Upload
from DBApp.forms import EmployeeForm,SignUpForm,UploadForm
from django.conf import settings
from django.core.mail import send_mail


from  django.contrib.auth.decorators import login_required
def home(request):
    return render(request,'DBApp/home.html')
def welcome(request):
    return render(request,'DBApp/welcome.html')

@login_required
def viewEmp(request):
    #fetch data from DB select * from Employee
    emplist=Employee.objects.all()
    #select * from Employee where ename='sumit'
    #emplist=Employee.objects.filter(ename='Sumit')
    #print(emplist)
    mydict={'emplist':emplist}
    return render(request,'DBApp/viewemp.html',context=mydict)

@login_required
def AddEmp(request):
    empform=EmployeeForm();
    mydict={'empform':empform}
    if request.method=='POST':
        #DB insert code goes here
        empform=EmployeeForm(request.POST);
        empform.save();#insert query
        print("Data inserted")
        mydict.update({'msg':'Employee Registered Successfully'})
    return render(request,'DBApp/addnewemp.html',context=mydict)

def SignUpPage(request):
    signupform=SignUpForm()
    mydict={'signupform':signupform}
    if request.method=='POST':
        #DB insert code goes here
        signupform=SignUpForm(request.POST);
        if signupform.is_valid():
            user=signupform.save();#insert query
            user.set_password(user.password)
            user.save()# this object save finally
            subject="EMS Welcome Mail"
            message="Welcome "+user.email+", You are register"
            recipient_list=[user.email]
            email_from=settings.EMAIL_HOST_USER
            send_mail(subject,message,email_from,recipient_list)
            mydict.update({'msg':'Registered Successfully'})
    return render(request,'DBApp/signup.html',context=mydict)

'''
ERROR :  data is not validate
    if request.method=='POST':
        #DB insert code goes here
        signupform=SignUpForm(request.POST);
        if signupform.is_valid():
            user=signupform.save();#insert query
            user.set_password(user.password)
            user.save()# this object save finally
            mydict.update({'msg':'Registered Successfully'})






'''
@login_required
def UploadView(request):
    uploadform=UploadForm()
    mydict={'uploadform':uploadform}
    if request.method=='POST':
        uploadform=UploadForm(request.POST,request.FILES);
        if uploadform.is_valid():
            data=uploadform.save(commit=False)
            data.author=request.user
            data.save()
            mydict.update({'msg':'Data Saved Successfully'})
    return render(request,'DBApp/upload.html',context=mydict)

@login_required
def ViewFilesView(request):
    images=Upload.objects.all().order_by('-upload_date')
    return render(request,'DBApp/viewfiles.html',{'images':images})

@login_required
def DetailView(request,pid):
    #select * from product where id='1'
    images=Upload.objects.get(id=pid)
    #images.delete();  delete records
    return render(request,'DBApp/detailview.html',{'images':images})


def DeleteProductView(request,pid):
    images=Upload.objects.get(id=pid)
    images.delete(); #delete records
    images=Upload.objects.all().order_by('-upload_date')
    return render(request,'DBApp/viewfiles.html',{'images':images,'msg':'Product Deleted'})







#
