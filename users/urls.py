from django.urls import path
from . import views
from django.contrib.auth.views import (
    PasswordChangeView, 
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    )
from django.urls import reverse, reverse_lazy

from django.views.decorators.cache import cache_page

app_name="users"

urlpatterns =[
    #path('register/', views.register, name='register'),
    path('register/', views.RegisterUser.as_view(), name="register"),
    #path('login_user/', views.login_user, name='login_user'),
    path('login_user/', views.LoginUser.as_view(), name="login_user"),
    #path('profile/', views.profile, name='profile'),
    path('profile/', cache_page(30)(views.Profile.as_view()), name='profile'),
    path('logout_user/', views.logout_user, name='logout_user'),

    # path('password-change/', PasswordChangeView.as_view(success_url = reverse_lazy("users:password_change_done"),
    # template_name = "users/password_change_form.html",
    # title = ("Password change")), name="password_change"),
    path('password-change/', views.UserPasswordChange.as_view(), name="password_change"),
    path('password-change/done', PasswordChangeDoneView.as_view(
        template_name = "users/password_change_done.html",title = ("Password change successful")
        ), name="password_change_done"),

    path("password_reset/", 
         PasswordResetView.as_view(template_name="users/password_reset_form.html",
                            email_template_name="users/password_reset_email.html",
                            success_url=reverse_lazy("users:password_reset_done")),
                            name="password_reset"),
    path("password_reset_done/", 
         PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), 
         name="password_reset_done"),
    path("password_reset_confirm/<uidb64>/<token>/", 
        PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html",
            success_url=reverse_lazy("users:password_reset_complete")),name="password_reset_confirm"),
    path("password_reset_complete/", 
         PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),
         name="password_reset_complete"),
]