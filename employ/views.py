from django.shortcuts import render
from .models import *

# Create your views here.
def main(request):
    return render(request, 'login.html') 

def employ(request):
    employlist=employid.objects.all()
    return render(request,'dashboard.html',{'list':employlist})