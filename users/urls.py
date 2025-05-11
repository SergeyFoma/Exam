from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse, reverse_lazy

app_name="users"

urlpatterns =[
    #path('register/', views.register, name='register'),
    path('register/', views.RegisterUser.as_view(), name="register"),
    #path('login_user/', views.login_user, name='login_user'),
    path('login_user/', views.LoginUser.as_view(), name="login_user"),
    #path('profile/', views.profile, name='profile'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('logout_user/', views.logout_user, name='logout_user'),

    # path('password-change/', PasswordChangeView.as_view(success_url = reverse_lazy("users:password_change_done"),
    # template_name = "users/password_change_form.html",
    # title = ("Password change")), name="password_change"),
    path('password-change/', views.UserPasswordChange.as_view(), name="password_change"),
    path('password-change/done', PasswordChangeDoneView.as_view(
        template_name = "users/password_change_done.html",title = ("Password change successful")
        ), name="password_change_done"),
]