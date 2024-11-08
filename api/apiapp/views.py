from django.shortcuts import render,redirect
from rest_framework.response import Response
from .models import travels
from .serializer import tserial
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['get','post'])
def index(request):
    if request.method=="GET":
        a=travels.objects.all()
        serializer=tserial(a,many=True)
        return Response(serializer.data)
    #post  method this is to insert new data
    if request.method=='POST':
         a=tserial(data=request.data)
         if a.is_valid():
             a.save()
             return Response(a.data)     
@api_view(['get','put','delete'])
def update(request,pk):
    a=travels.objects.get(id=pk)
    if request.method=='GET':
        serializer=tserial(instance=a)
        return Response(serializer.data)
    if request.method=='PUT':
        b=tserial(instance=a,data=request.data)
        if b.is_valid():
            b.save()
            return Response(b.data)
    if request.method=='delete':
        a.delete()
        return redirect('home')
    
    