from django.shortcuts import render
import requests
import json


# Create your views here.
def signup(request):
    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')


def submitUser(request):
    email = request.GET['Emailid']
    password = request.GET['Password']
    name = request.GET['Username']
    print(email, password, name, "this is me")

    url = "http://127.0.0.1:8000/api/login/"

    payload = {'email': email, 'password': password, 'name': name}
    payload = json.dumps(payload)
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.text
    return render(request, 'temp.html', {'data': data})

def sUser(request):

    email = request.GET['Emailid']
    password = request.GET['Password']
    name = request.GET['Username']
    print(email, password, name, "welcome")

    url = "http://127.0.0.1:8000/api/login/"

    payload = {'email': email, 'password': password, 'name': name}
    payload = json.dumps(payload)
    headers = {
         'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.text
    return render(request, 'temp.html', {'data': data})