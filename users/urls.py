from django.urls import path
from . import views

app_name="users"

urlpatterns =[
    #path('register/', views.register, name='register'),
    path('register/', views.RegisterUser.as_view(), name="register"),
    #path('login_user/', views.login_user, name='login_user'),
    path('login_user/', views.LoginUser.as_view(), name="login_user"),
    path('profile/', views.profile, name='profile'),
    path('logout_user/', views.logout_user, name='logout_user'),
]