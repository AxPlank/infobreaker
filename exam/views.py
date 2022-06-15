from django.shortcuts import render, get_object_or_404
from .models import *

def written(request):
    part_list = WrittenPart.objects.order_by('part')
    dictt = {'part_list': part_list}
    return render(request, 'exam/written.html', dictt)

def writtenPart(request, part):
    dictt = {}
    if part == 1:
        question_list = WrittenQuestion.objects.filter(part=part).order_by('id')
        dictt['quesiton_list'] = question_list
    if part == 2:
        question_list = WrittenQuestion.objects.filter(part=part).order_by('id')
        dictt['quesiton_list'] = question_list
    if part == 3:
        question_list = WrittenQuestion.objects.filter(part=part).order_by('id')
        dictt['quesiton_list'] = question_list
    if part == 4:
        question_list = WrittenQuestion.objects.filter(part=part).order_by('id')
        dictt['quesiton_list'] = question_list
    if part == 5:
        question_list = WrittenQuestion.objects.filter(part=part).order_by('id')
        dictt['quesiton_list'] = question_list
    return render(request, 'exam/question_choice.html', dictt)

def practical(request):
    part_list = PracticalPart.objects.order_by('part')
    dictt = {'part_list': part_list}
    return render(request, 'exam/practical.html', dictt)

def practicalPart(request, part):
    return render(request, 'exam/question_choice.html')

# Create your views here.
