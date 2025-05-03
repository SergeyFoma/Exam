from django.shortcuts import render
from users.forms import RegisterUserForm, LoginUserForm, ProfileUserForm
from django.urls import reverse, reverse_lazy 
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from plumber.models import AnswersUser, Mashine
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView

# def register(request):
#     if request.method=="POST":
#         form=RegisterUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("users:login_user"))

#     else:
#         form=RegisterUserForm()
#     context={
#         'form':form,
#     }
#     return render(request, "users/register.html", context)
class RegisterUser(CreateView):
    form_class=RegisterUserForm
    template_name="users/register.html"
    extra_context={"title":"Регистрация"}
    success_url=reverse_lazy("users:login_user")




# def login_user(request):
#     if request.method=='POST':
#         form=LoginUserForm(data=request.POST)
#         if form.is_valid():
#             username=request.POST['username']
#             password=request.POST['password']
#             user=authenticate(username=username, password=password)
#             if user and user.is_active:
#                 login(request,user)
#                 #messages.success(request,f'{username}, Вы вошли в аккаунт.')
#                 return redirect(reverse("users:profile"))
            

#     else:
#         form=LoginUserForm()
#     context={
#         'form':form,
#     }
#     return render(request, "users/login_user.html", context)

class LoginUser(LoginView):
    form_class=LoginUserForm
    template_name="users/login_user.html"
    extra_context={"title":"Authorization"}
    def get_success_url(self):
        return reverse_lazy("users:profile")

@login_required
def profile(request):
    mashine=Mashine.objects.all()
    
    if request.method == "POST":
        form=ProfileUserForm(request.POST, request.FILES, instance = request.user)
        if form.is_valid():
            form.save()
            #return redirect(reverse("users:profile"))
    else:
        form=ProfileUserForm()
    
    context={
        'form':form,
        'mashine':mashine,
    }
    return render(request, "users/profile.html", context)

def logout_user(request):
    AnswersUser.objects.filter(name_user=request.user.username).delete()
    logout(request)
    return redirect(reverse("plumber:index"))