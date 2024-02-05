from django.shortcuts import render,HttpResponse

# Create your views here.

def wish(request):
    message = '<h1>Hello How are you </h1>'
    return HttpResponse(message)