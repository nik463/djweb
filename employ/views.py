from django.shortcuts import render
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

# Create your views here.
def main(request):
    return render(request, 'home.html') 

def employ(request):
    employlist=employid.objects.all()
    return render(request,'dashboard.html',{'list':employlist})

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"