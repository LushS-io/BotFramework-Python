from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("<em>Begin MarkBot</em>")


def control(request):
    return HttpResponse("Control Dashboard exists here!")
