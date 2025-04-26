from django.shortcuts import render
from plumber.models import Questions, Answers, AnswersUser
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy 
#from plumber.utils import redir
from plumber.forms import TestForm
from django.shortcuts import get_object_or_404
from plumber.models import Mashine

def index(request):
    context={

    }
    return render(request, "plumber/index.html", context)

def vibor(request):
    mashine=Mashine.objects.all()
    context={
        'mashine':mashine,
    }
    return render(request, "plumber/vibor.html", context)

#que_count_list=[]
que_count=int()
answ=''
que=''
def testing(request, t_slug):
    mash=get_object_or_404(Mashine, slug=t_slug)
    global que
    que=Questions.objects.filter(mash=mash).order_by('pk')
    global que_count
    que_count=Questions.objects.filter(mash=mash).count()
    #print(que)
    global answ
    answ=Answers.objects.filter(mash=mash).order_by('pk')
    #print(type(mash))
    #que_count_list.append(que_count)
    
    context={
        'mash':mash,
        'que':que,
        'answ':answ,   
        
    }
    return render(request, "plumber/testing.html", context) 


def answer(request):
    name=request.user.username
    #alist=[]
    for key, value in request.GET.items():
        #res2=f'{key}:{value}'
        #alist.append(res2)
        #print('answer===', res2)
        answers=AnswersUser.objects.create(name_user=name, question=key, answer=value)
        answers.save()
        

        # with open(f'{name}.txt', 'a+', encoding='UTF-8')as f:
        #     f.write(res2+'\n')
    # context={
    #     'name':name,
    # }
    #return render(request, "plumber/answer.html", context)
    return redirect(reverse("plumber:answer2"))

def answer2(request):
    # for i in answ:
    #     print(i.answer)
    #print('QUE_COUNT_LIST===',que_count_list[0:])
    #mash=get_object_or_404(Mashine, slug=mash_slug)
    #que_num=Questions.objects.filter(mash=mash).count
    # que_num=Questions.objects.all().count()#всего вопросов
    # print(que_num)
    ans=AnswersUser.objects.all().order_by('pk')

    answers=Answers.objects.all().order_by('pk')
    answertrue=AnswersUser.objects.filter(answer='Верно').count()
    answerfalse=AnswersUser.objects.filter(answer='Не верно').count()
    ques_res=answertrue+answerfalse #решенных вопросов

    # for i in que_count_list:    
    #     print(i)
    #print('IIII-',i)
    variance=round(ques_res/que_count*100,2) #отклонение
    percent=round((answertrue/(answertrue+answerfalse)*100),2)-(100-variance)#правильных ответов
    #que=Questions.objects.all()

    context={
        'answ':answ,
        'answers':answers,
        'answertrue':answertrue,
        'answerfalse':answerfalse,
        'variance':variance,
        'percent':percent,
        #'que_num':que_num,
        'ques_res':ques_res,
        'que_count':que_count,
        'que':que,
        #'que_count_list':que_count_list,
        'ans':ans,
    }
    return render(request, "plumber/answer2.html", context)