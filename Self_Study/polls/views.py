from django.http import HttpResponse
from django.http import Http404

from django.shortcuts import render,get_object_or_404
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}

    # render함수는 1:request 객체를 첫번째 인수로 받고,
    #            2:template 이름을 두번째 인수로 받고,
    #            3:context 사전형 객체를 세번째 선택적(optional) 인수로 받습니다.
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    # (1) 방식
    # -> Question does not exist!
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist!")
    # return render(request, "polls/detail.html", {"question": question})
    # (2) 방식
    # -> No Question matches the given query
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on questions %s." %question_id)
