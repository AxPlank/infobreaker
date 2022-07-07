from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from main.forms import SingupForm

# Create your views here.

def mainpage(request):
    return render(request, 'main/main.html')

def signup(request):
    if request.method == "POST" and SingupForm(request.POST).is_valid():
        form = SingupForm(request.POST)
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        return redirect('main:main')
    else:
        form = SingupForm
        return render(request, 'main/signup.html', {'form': form})