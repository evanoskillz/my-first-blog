from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h3>Hello, world. You are at the polls index.<br> First Django Application</h3>")

