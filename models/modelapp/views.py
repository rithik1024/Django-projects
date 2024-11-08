from django.shortcuts import render,redirect
from modelapp.models import Student
def index(request):   
    
    if request.method=="POST":
        addname=request.POST.get("name1")
        addage=request.POST.get("age1")
        addlocation=request.POST.get("location1")
        Student.objects.create(name=addname,age=addage,location=addlocation)
    var=Student.objects.all()
    context={
    'var': var
    }
    return render(request,"index.html",context)
def list(request,pk):
    var=Student.objects.get(id=pk)
    context={
        'var':var
    }
    if request.method=='POST':
        if 'delete' in request.POST:
         var.delete()
         return redirect("Home")
    return render(request,"list.html",context) 

def edit(request,pk):
    var=Student.objects.get(id=pk)
    if request.method=='POST':
        newname1=request.POST.get("newname")
        newage1=request.POST.get("newage")
        newlocation1 =request.POST.get("newlocation")
        var.name=newname1
        var.age=newage1
        var.location=newlocation1
        var.save()
        return redirect("Home")
        
    return render(request,"edit.html",{'var':var})