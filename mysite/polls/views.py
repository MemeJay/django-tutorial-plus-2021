from http.client import HTTPResponse
from tkinter.messagebox import QUESTION
from django.shortcuts import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_ID):
    return HttpResponse("You're looking at question %s." % question_ID)

def results(request, question_ID):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_ID)

def vote(request, question_ID):
    return HttpResponse("You're voting on question %s.")