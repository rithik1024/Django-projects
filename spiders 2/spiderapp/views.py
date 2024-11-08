
from django.shortcuts import render,redirect
from .models import Student
# Create your views here.
def index(request):
  if request.method=="POST":
      name=request.POST.get("name1")
      result=request.POST.get("result")
      if name and result:
        Student.objects.create(name=name,result=result) 

  return render(request,'index.html')
def add(request):
    var=Student.objects.last()
    if request.method=="POST":
      return redirect('list')
    return render(request,'add.html',{'var':var})
  
def list(request):
   var=Student.objects.all()
   return render(request,'list.html',{'var':var})
 