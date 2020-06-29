from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"first_app/home1.html")

def index1(request):
    return render(request,"first_app/loginpage.html")