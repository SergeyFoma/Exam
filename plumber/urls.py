from django.urls import path
from . import views

app_name="plumber"

urlpatterns = [
    path('', views.index, name='index'),
    path('testing/', views.testing, name='testing'),
]