from django.shortcuts import render
from plumber.models import Questions, Answers, AnswersUser
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy 
#from plumber.utils import redir
from plumber.forms import TestForm

def index(request):
    context={

    }
    return render(request, "plumber/index.html", context)

def testing(request):
    que=Questions.objects.all()
    ans=Answers.objects.all()
    
    context={
        'que':que,
        'ans':ans,
        #'query':query,
        
    }
    return render(request, "plumber/testing.html", context) 


def answer(request):
    name=request.user.username
    #alist=[]
    for key, value in request.GET.items():
        res2=f'{key}:{value}'
        #alist.append(res2)
        #print('answer===', res2)
        answers=AnswersUser.objects.create(name_user=name, question=key, answer=value)
        answers.save()

        with open(f'{name}.txt', 'a+', encoding='UTF-8')as f:
            f.write(res2+'\n')
    context={
        'name':name,
    }
    #return render(request, "plumber/answer.html", context)
    return redirect(reverse("plumber:answer2"))

def answer2(request):
    que_num=Questions.objects.all().count()#всего вопросов
    ans=AnswersUser.objects.all()
    answers=Answers.objects.all()
    answertrue=AnswersUser.objects.filter(answer='Верно').count()
    answerfalse=AnswersUser.objects.filter(answer='Не верно').count()
    ques_res=answertrue+answerfalse #решенных вопросов
    variance=round(ques_res/que_num*100,2) #отклонение
    percent=round((answertrue/(answertrue+answerfalse)*100),2)-(100-variance)#правильных ответов
    que=Questions.objects.all()
    
    context={
        'ans':ans,
        'answers':answers,
        'answertrue':answertrue,
        'answerfalse':answerfalse,
        'percent':percent,
        'que_num':que_num,
        'ques_res':ques_res,
        'variance':variance,
        'que':que,
    }
    return render(request, "plumber/answer2.html", context)