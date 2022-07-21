from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='main:login')
def partChoice(request):
    written_list = WrittenPart.objects.order_by('part')
    practical_list = PracticalPart.objects.order_by('part')
    dictt = {'written_list': written_list,
             'practical_list': practical_list}
    return render(request, 'exam/part_choice.html', dictt)

@login_required(login_url='main:login')
def writtenPart(request, part):
    problem_list = Problem.objects.filter(type='필기', part=part).order_by('id')
    dictt = {'problem_list': problem_list}
    return render(request, 'exam/question_choice.html', dictt)

@login_required(login_url='main:login')
def practicalPart(request, part):
    problem_list = Problem.objects.filter(type='실기', part=part).order_by('id')
    dictt = {'problem_list': problem_list}
    return render(request, 'exam/question_choice.html', dictt)

@login_required(login_url='main:login')
def problem(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    dictt = {'problem': problem}
    return render(request, 'exam/problem.html', dictt)

@login_required(login_url='main:login')
def comment(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    dictt = {'problem': problem}
    return render(request, 'exam/comment.html', dictt)

@login_required(login_url='main:login')
def CBTChoice(request):
    return render(request, 'exam/CBT_choice.html')

@login_required(login_url='main:login')
def CBT_part(request, part):
    problem_list = Problem.objects.filter(type_integer=1, part=1).order_by('?')[:20]
    dictt = {}
    for i in range(20):
        dictt[f'Q{i}'] = problem_list[i]
    return render(request, 'exam/CBT_parttest.html', dictt)