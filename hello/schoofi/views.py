from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect,reverse
from datetime import datetime
from schoofi.models import user
import mysql.connector
from operator import itemgetter
from django.contrib import messages
from django.contrib.auth import authenticate,logout
from datetime import date
from django.contrib import auth





# Create your views here.

def index(request):
    #messages.success(request," Message has been sent successfully ! ")
    return render(request,'index.html')
    


def about(request):
    return render(request,'about.html')

def contact(request): 
    
    return render(request,'contact.html')
def services(request):
    return render(request,'services.html')


def signup(request):
    if request.method=='POST':
        User=user()
        User.Name=request.POST.get('Name')
        User.School=request.POST.get('School')
        User.Rollno=request.POST.get('Rollno')
        User.Email=request.POST.get('Email')
        User.Password=request.POST.get('Password')
        User.Confirmpass=request.POST.get('Confirmpass')
        if User.Password !=User.Confirmpass:
            messages.success(request,'password not matched')
            return redirect('signup')

        elif User.Name == "" or User.Password =="":
            messages.success(request,'please enter details')
            return redirect('signup')
        else:
            User.save()
            messages.success(request,'New User'+request.POST.get('Name')+"Added Successfully")
            return render(request,'register.html')
    else:
        return render(request,'register.html')


def loginsystem(request):
    conn= mysql.connector.connect(host="localhost",user="root",password="",database='vidmeet')
    cursor=conn.cursor()
    if request.method == "POST":
        Username1=request.POST['Email']
        Password1=request.POST['Password']
        print(Username1)
        print(Password1)
        sqlcommand="select * from schoofi_user where Email=%s and Password=%s"
        params=(Username1,Password1)
        cursor.execute(sqlcommand,params)
        data=cursor.fetchall()
        print(data)
        if len(data)>0:
            return redirect('/classifiadmin')
        else:
            return render(request,"login.html")
    else:
        return render(request,'login.html')




def classifiadmin(request):
    return render(request,'classifiadmin.html')

def assignments(request):
    return render(request,'assignments.html')

def logoutsystem(request):
    if request.method== "POST":
        logout(request)
        return HttpResponseRedirect(reverse('loginsystem'))
    return redirect('/loginsystem')

def attendance(request):
    conn= mysql.connector.connect(host="localhost",user="root",password="",database='vidmeet')
    cursor=conn.cursor()
    today=date.today()
    print(today)
    cursor.execute("select rollno from attendancestudent where presentdate= %s",[today])
    
    rollnodata=[row[0] for row in cursor.fetchall()]
    print(rollnodata)
    cursor.execute("select * from attendancestudent where presentdate= %s",[today])
    data=cursor.fetchall()
    print(data)
    print (rollnodata)
    cursor.execute("select id,Name,Rollno from schoofi_user ")
    dataschoofirollno=cursor.fetchall()
    print(dataschoofirollno)

   
    
    len1=len(dataschoofirollno)
    len2=len(rollnodata)
    for i in range (len1):
        for j in range (len2):
            if dataschoofirollno[i]==rollnodata[j]:
                datasend='present'
            else:
                datasend='absent'

  
    
 

    return render(request,'attendance.html', {'attendance':data,'rollnodata':rollnodata,'presentdate':today,'dataschoofiroll':dataschoofirollno })


def profile(request):
    return render(request,'profile.html')

