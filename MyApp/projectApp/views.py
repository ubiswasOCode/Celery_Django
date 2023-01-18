from django.shortcuts import render
from django.http import HttpResponse
from .task import *

# Create your views here.
def Index(request):
    Main_task.delay(10)
    return HttpResponse("Hello bro good night")