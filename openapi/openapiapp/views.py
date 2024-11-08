from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    data=None
    if request.method=='POST':
      search=request.POST.get("search")
    # a=requests.get("https://restcountries.com/v2/all")
    # data=a.json()
      a=requests.get(f"https://restcountries.com/v2/name/{search}")
      data=a.json()
    return render(request,'index.html',{'data':data})