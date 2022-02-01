from http.client import HTTPResponse
from tkinter.messagebox import QUESTION
from django.shortcuts import HttpResponse
from django.template import loader

from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_ID):
    return HttpResponse("You're looking at question %s." % question_ID)

def results(request, question_ID):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_ID)

def vote(request, question_ID):
    return HttpResponse("You're voting on question %s.")