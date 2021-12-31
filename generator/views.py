from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html',{"password":"kjdkjdj"})
    
def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    thepassword = ''
    length = int(request.GET.get("length"))
    if request.GET.get("uppercase"):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get("Numbers"):
        characters.extend(list('1234567890'))
    if request.GET.get("Special"):
        characters.extend(list('~!@#$%^&*()_+'))
        
    for x in range(length):
        thepassword+= "Happy New year Pillakai"
        #thepassword+= random.choice(characters)
    return render(request,'generator/password.html',{"password":thepassword})
    
    
def about(request):
    return render(request,'generator/about.html')

