from django.shortcuts import render,HttpResponse
import datetime

# Create your views here.
def tellTimeNow(request):
    time = datetime.datetime.now()
    return HttpResponse(f'<h1>Current time is : {time}</h1>')