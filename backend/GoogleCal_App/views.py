from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def app_index(request):
    return HttpResponse("You have found Homepage of MarkBot, click next to learn more!")


def bot(request):
    my_dict = {'insert_me': "Hello I am MarkBot, please to meet you! I can assist putting Toggl entries onto Google Calendar!"}
    return render(request, 'GoogleCal_App/index.html', context=my_dict)


def dash(request):
    return HttpResponse("Bot Config Dashboard exists here!")
