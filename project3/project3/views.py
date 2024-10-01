from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
# FILE UPLOAD AND VIEW
from  django.core.files.storage import FileSystemStorage
# SESSION
from django.conf import settings


def first(request):
    return render(request,'index.html')

def login(request):
    return render(request,'demo.html')

def profile():
    return render('index.html')


def logreg(request):
   
    a=request.POST.get('email')
    b=request.POST.get('password')

    if (a== 'admin@gmail.com' and b=='admin'):
        request.session['logint']='a'
        request.session['logint']='b'
        return render(request,'index.html')
    
    elif(register.objects.filter(email=a, password=b).exists()):
        user=register.objects.get(email=a, password=b)
        request.session['uid']=user.id
        return render(request,'index.html')
    
    else:
        return render(request,'demo.html')

def reg(request):
    return render(request,'new.html')

def addreg(request):
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('phone')
        d=request.POST.get('password')

        x=register(name=a,email=b,phone=c,password=d)
        x.save()
    
    return render(request,'index.html')

def logout(request):
    session_keys=list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(first)

def viewuser(request):
    a=register.objects.all()
    return render(request,'select.html',{'result':a})

def profile(request):
    sel=register.objects.get(id=request.session['uid'])
    return render(request,'newone.html',{'result':sel})

def deleteuser(request,id):
    sel=register.objects.get(id=id)
    sel.delete()
    return redirect(viewuser)

def update(request,id):
    sel=register.objects.get(id=id)
    return render(request,'update.html',{'result':sel})





def addupdate(request,id):
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('phone')
        d=request.POST.get('password')

        x=register(name=a,email=b,phone=c,password=d,id=id)
        x.save()
    
    return redirect(viewuser)
