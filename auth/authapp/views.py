from django.shortcuts import render,redirect
from .forms import MyForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages 
# Create your views here\
def index(request):
    form = MyForm()
    if request.method=="POST":
        username1=request.POST['username']
        password1=request.POST['password1']
        user = User.objects.create(username=username1)
        user.set_password(password1)
        user.save()
        print("success")
        return redirect("login")
    return render(request,"index.html",{'form':form})
def log(request):
    if request.method=="POST":
        un = request.POST['un']
        password=request.POST["password"]
        user = User.objects.get(username=un)
        user = authenticate(request,username=un,password=password)
        if user is not None:
            login(request,user)
            print("login successful")
            return redirect ('dash')
        else:
            return redirect('login')
    return render(request,"log.html")
def dash(request):
    return render(request,'dash.html')

