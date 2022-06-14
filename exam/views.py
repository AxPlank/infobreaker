from django.shortcuts import render
from django.http import HttpResponse

def written(request):
    return render(request, 'exam/written.html')

def practical(request):
    return render(request, 'exam/practical.html')

# Create your views here.
