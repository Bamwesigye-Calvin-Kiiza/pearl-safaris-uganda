from django.shortcuts import render

# Create your views here.
def homepage(request):
    welcome = {'msg':'Welcome to Pearl Safaris Uganda'}
    return render(request,'pearlsafaris/home.html',context=welcome)
