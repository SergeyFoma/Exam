from django.shortcuts import render
from plumber.models import Questions, Answers, AnswersUser
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse, FileResponse, Http404
from django.urls import reverse, reverse_lazy 

from plumber.forms import TestForm
from django.shortcuts import get_object_or_404
from plumber.models import Mashine, Professions, FileResult
from materials.models import UploadedFile
import os
import subprocess
from exam import settings
from django.views.generic import ListView

from bs4 import BeautifulSoup 
import requests
import lxml
from datetime import datetime

class Index(ListView):
    model=UploadedFile
    template_name='plumber/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Test online. Тестирование работников основных и смежных профессий'
        context['content_description'] = 'Тесты для слесарей-ремонтников НПО, стропальщиков и сварщиков'
        return context
    def get_queryset(self):
        return UploadedFile.objects.all()
    def get_queryset(self):
        return Professions.objects.all()


def vibor(request):
    mashine=Mashine.objects.all()
    context={
        'mashine':mashine,
    }
    return render(request, "plumber/vibor.html", context)


mash=''
que_count=int()
answ=''
que=''
def testing(request, t_slug):
    global mash
    mash=get_object_or_404(Mashine, slug=t_slug)
    global que
    que=Questions.objects.filter(mash=mash).order_by('pk')
    global que_count
    que_count=Questions.objects.filter(mash=mash).count()
    global answ
    answ=Answers.objects.filter(mash=mash).order_by('pk').select_related("ques")
    title=f'Test online. Страница тестирования.{mash}'
    context={
        'mash':mash,
        'que':que,
        'answ':answ,   
        'que_count':que_count,
        'title':title,
    }
    return render(request, "plumber/testing.html", context) 


def answer(request):
    name=request.user.username
    for key, value in request.GET.items():
        answers=AnswersUser.objects.create(name_user=name, question=key, answer=value)
        answers.save()

    return redirect(reverse("plumber:answer2"))

def answer2(request):
    title="Test online. Результаты теста."
    ans=AnswersUser.objects.all().order_by('pk')
    answers=Answers.objects.all().order_by('pk').select_related("ques")
    answertrue=AnswersUser.objects.filter(answer='Верно').count()
    answerfalse=AnswersUser.objects.filter(answer='Не верно').count()
    ques_res=answertrue+answerfalse #решенных вопросов
    variance=round(ques_res/que_count*100,2) #отклонение
    percent_true=(answertrue*100)/que_count

    context={
        'answ':answ,
        'answers':answers,
        'answertrue':answertrue,
        'answerfalse':answerfalse,
        'variance':variance,
        'ques_res':ques_res,
        'que_count':que_count,
        'que':que,
        'ans':ans,
        'mash':mash,
        'percent_true':percent_true,
        'title':title,
    }
    return render(request, "plumber/answer2.html", context)


def parser(request):
       #парсим страницу с результатом(answer2) и записываем в result.txt
    now=datetime.now()

    url = "http://127.0.0.1:8000/answer2/"
    #url = "https://test-online.ru:8000/answer2/"
    response = requests.get(url)
    bs=BeautifulSoup(response.text,'lxml')

    temp1=bs.find(class_='result').find('b')
    temp2=bs.find(class_='result').find('h2')
    with open(f'./media/uploads/result/{request.user.last_name}-{request.user.first_name}-{temp1.text}-{request.user.username}.txt','w+',encoding='UTF-8')as f:
        f.write(f'{request.user.last_name}-{request.user.first_name}-{request.user.username}. {now.strftime("%d.%m.%Y")}\n{temp2.text}\n')

    temp3=bs.find(class_='result').find_all('p')
    for x in temp3:
        with open(f'./media/uploads/result/{request.user.last_name}-{request.user.first_name}-{temp1.text}-{request.user.username}.txt','a',encoding='UTF-8')as f:
            f.write(f'{x.text}\n')
    return redirect(reverse("users:logout_user"))

def result(request):
    file_path = os.path.join(settings.MEDIA_ROOT)
    path2="/uploads/result/"
    path3=file_path+path2
    pth=os.listdir(path3)
    ilist=[]
    pat="../media/uploads/result/"
    for i in pth:
        ilist.append(pat+i)
        
    context={
        'ilist':ilist,
    }
    return render(request,"plumber/result.html",context)


def delete_file(request,name):
    file_path2 = os.path.join(settings.MEDIA_ROOT)
    path3=file_path2 + f"/uploads/result/{name}"
    os.remove(path3)   
    return render(request,"plumber/delete_file.html",{'name':name})


