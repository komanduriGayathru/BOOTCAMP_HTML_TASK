from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"first_app/home.html")

def index2(request):
    return render(request,"first_app/payment.html")

def index3(request):
    return HttpResponse("Hello welcome to project")