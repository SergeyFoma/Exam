from django.shortcuts import render
from users.forms import RegisterUserForm, LoginUserForm
from django.urls import reverse, reverse_lazy 
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages

def register(request):
    if request.method=="POST":
        form=RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form=RegisterUserForm()
    context={
        'form':form,
    }
    return render(request, "users/register.html", context)

def login_user(request):
    if request.method=='POST':
        form=LoginUserForm(data=request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username, password=password)
            if user:
                auth.login(request,user)
                messages.success(request,f'{username}, Вы вошли в аккаунт.')
            return redirect(reverse("plumber:testing"))
            

    else:
        form=LoginUserForm()
    context={
        'form':form,
    }
    return render(request, "users/login_user.html", context)
