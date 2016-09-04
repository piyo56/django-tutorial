from django.shortcuts import render
from django.http import HttpResponse

def top(request):
    print(request)
    return HttpResponse("<h1>Hello, world!</h1>")
