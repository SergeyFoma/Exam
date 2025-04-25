from django.urls import path
from . import views

app_name="plumber"

urlpatterns = [
    path('', views.index, name='index'),
    path('testing/', views.testing, name='testing'),
    path('answer/', views.answer, name='answer'),
    path('answer2/', views.answer2, name='answer2'),
]