from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
def homepage(request):
    welcome = {'msg':'Welcome to Pearl Safaris Uganda'}
    return render(request,'pearlsafaris/home.html',context=welcome)

def signUp_page(request):
    if request.method == 'POST':
        newuser = SignUp(request.POST)
        if newuser.is_valid():
            newuser.save(commit=True)
            return homepage(request)
    else:
        newuser = SignUp()  
    return render(request,'pearlsafaris/signUp.html',{'new_user':newuser})

def users_list(request):
    user = User.objects.all
    return render(request,'pearlsafaris/userlist.html',{'users':user})