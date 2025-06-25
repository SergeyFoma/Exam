from django.shortcuts import render
from plumber.models import Questions, Answers, AnswersUser
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse, FileResponse, Http404
from django.urls import reverse, reverse_lazy 
#from plumber.utils import redir
from plumber.forms import TestForm
from django.shortcuts import get_object_or_404
from plumber.models import Mashine, Professions
from materials.models import UploadedFile
import os
import subprocess
from exam import settings
from django.views.generic import ListView

from bs4 import BeautifulSoup 
import requests
import lxml
from datetime import datetime

# def index(request):
#     pfus=UploadedFile.objects.all()
#     context={
#         'pfus':pfus,
        
#     }
#     return render(request, "plumber/index.html", context)
class Index(ListView):
    model=UploadedFile
    template_name='plumber/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Главная страница'
        return context
    def get_queryset(self):
        return UploadedFile.objects.all()
    def get_queryset(self):
        return Professions.objects.all()


# def file_pdf(request, ind_id):
#     pfu=get_object_or_404(UploadedFile,id=ind_id)
#     st=str(pfu.file)
#     path1=str(settings.MEDIA_ROOT)
#     path2='uploads'
#     pf=os.listdir(path1+'/'+path2)
#     for i in pf:
#         if path2+'/'+i == st:
#             start_pdf=subprocess.Popen([path1+'/'+path2+'/'+i], shell=True)
#             #return redirect(reverse("plumber:index"))
#             return redirect(reverse('materials:category_post', kwargs={'cat_id':2}))
    # context={
    #     'pfu':pfu,
    # }
    # return render(request, "plumber/file_pdf.html", context)

def vibor(request):
    mashine=Mashine.objects.all()
    context={
        'mashine':mashine,
    }
    return render(request, "plumber/vibor.html", context)

#que_count_list=[]
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
    #print(que)
    global answ
    answ=Answers.objects.filter(mash=mash).order_by('pk')
   
    #print(type(mash))
    #que_count_list.append(que_count)
    context={
        'mash':mash,
        'que':que,
        'answ':answ,   
        'que_count':que_count,
    }
    return render(request, "plumber/testing.html", context) 


def answer(request):
    name=request.user.username
    for key, value in request.GET.items():
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
    #percent=round((float(answertrue)/(float(answertrue)+float(answerfalse))*100),2)-(100-float(variance))#правильных ответов
    #que=Questions.objects.all()
    percent_true=(answertrue*100)/que_count
    

    context={
        'answ':answ,
        'answers':answers,
        'answertrue':answertrue,
        'answerfalse':answerfalse,
        'variance':variance,
        #'percent':percent,
        #'que_num':que_num,
        'ques_res':ques_res,
        'que_count':que_count,
        'que':que,
        #'que_count_list':que_count_list,
        'ans':ans,
        'mash':mash,
        'percent_true':percent_true,
    }
    return render(request, "plumber/answer2.html", context)



# def file_pdf(request):
#     start_pdf=os.startfile('./files_pdf/one.pdf')
#     return render(request, 'plumber/file_pdf.html', {'start_pdf':start_pdf})

def parser(request):
       #парсим страницу с результатом(answer2) и записываем в result.txt
    now=datetime.now()

    url = "http://127.0.0.1:8000/answer2/"
    response = requests.get(url)
    bs=BeautifulSoup(response.text,'lxml')

    temp1=bs.find(class_='result').find('b')
    temp2=bs.find(class_='result').find('h2')
    with open(f'./media/uploads/result/{request.user.last_name}-{temp1.text}-{request.user.username}.txt','w+',encoding='UTF-8')as f:
        f.write(f'{request.user.last_name}-{request.user.username}. {now.strftime("%d.%m.%Y")}\n{temp2.text}\n')

    temp3=bs.find(class_='result').find_all('p')
    for x in temp3:
        with open(f'./media/uploads/result/{request.user.last_name}-{temp1.text}-{request.user.username}.txt','a',encoding='UTF-8')as f:
            f.write(f'{x.text}\n')
    
    #return render(request, "plumber/parser.html",context)
    return redirect(reverse("users:logout_user"))

def result(request):
    context={

    }
    return render(request,"plumber/result.html",context)

def download(request):
    file_path = os.path.join(settings.MEDIA_ROOT)
    path2="/uploads/result/"
    path3=file_path+path2
    print("file_path==========",file_path)
    print("PATH3======",path3)
    name="DerF-Сварочные работы-DERF.txt"
    path4=path3+name
    print("PATH4======",path4)
    if os.path.exists(path4):
        with open(path4, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename='+name 
            return response
    raise Http404