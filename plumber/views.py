from django.shortcuts import render
from plumber.models import Questions, Answers

def index(request):
    context={

    }
    return render(request, "plumber/index.html", context)

def testing(request):
    que=Questions.objects.all()
    ans=Answers.objects.all()
    query = request.GET.get('q')
    #print(query)
    # if request.method=='GET':
    #     print(query)
    #print(request.GET.get('radio',''))
    nam=request.user.username
    # res=request.GET.get('radio','')
    # print(res)
    # with open('f3.txt','a',encoding="utf-8")as f:
    #     f.write(res)
    for key, value in request.GET.items():
        res2=f'{key}:{value}'
        print(res2)
        
    #     with open(f'{nam}.txt','a+',encoding="utf-8")as f:
    #         f.write(res2+'\n')
    #         #print(nam)
   
    
    context={
        'que':que,
        'ans':ans,
        'query':query,
        
    }
    return render(request, "plumber/testing.html", context) 
