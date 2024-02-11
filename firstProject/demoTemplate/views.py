from django.shortcuts import render
import datetime

# Create your views here.
def display(request):
    date = datetime.datetime.now()
    hour = date.strftime('%H')
    if int(hour) < 12:
        message = 'Good Morning'
    else:
        message = 'Good Afternoon'
    context = {
        'date' : date,
        'name' : 'Arun',
        'message' : message,
    }
    return render(request,'index.html',context)