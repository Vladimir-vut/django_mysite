from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Question


# Create your views here.


def index(request):
    try:
        latest_question_list = Question.objects.order_by('pub_date')[:5]
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'pools/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question
    }
    return render(request, 'pools/detail.html', context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question
    }
    return render(request, 'pools/results.html', context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question
    }
    return render(request, 'pools/vote.html', context)



