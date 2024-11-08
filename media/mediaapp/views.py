from django.shortcuts import render 
from .forms import mediaform
from .models import media
# Create your views here.
def index(request):
    form1=mediaform()
    if request.method=='POST':
        form1=mediaform(request.POST,request.FILES)
        if form1.is_valid():
            form1.save()
    
    data=media.objects.all()
    return render(request,"index.html", {'form1':form1,'data':data})


def details(request,pk):
    data=media.objects.get(id=pk)
    return (request,'deatils.html',{'data':data})

   