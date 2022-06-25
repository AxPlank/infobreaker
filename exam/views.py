from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import *

def written(request):
    part_list = WrittenPart.objects.order_by('part')
    dictt = {'part_list': part_list}
    return render(request, 'exam/written.html', dictt)

def writtenPart(request, part):
    problem_list = Problem.objects.get(type='필기', part=part).order_by('id')
    dictt = {'problem_list': problem_list}
    return render(request, 'exam/question_choice.html', dictt)

def practical(request):
    part_list = PracticalPart.objects.order_by('part')
    dictt = {'part_list': part_list}
    return render(request, 'exam/practical.html', dictt)

def practicalPart(request, part):
    problem_list = Problem.objects.get(type='실기', part=part).order_by('id')
    dictt = {'problem_list': problem_list}
    return render(request, 'exam/question_choice.html', dictt)

def problem(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    dictt = {'problem': problem}
    return render(request, 'exam/problem.html', dictt)

def checkAnswer(request, problem_id):
    if request.method == 'POST':
        answer = request.POST.get('ex', False)
        problem = Problem.objects.get(id=problem_id)
        if problem.id != answer:
            messages.error(request, "틀렸습니다.")
        else:
            messages.success(request, "정답입니다.")

        return redirect('exam:problem', problem_id=problem_id)


# Create your views here.
