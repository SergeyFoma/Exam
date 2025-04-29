from django.urls import path
from . import views

app_name="plumber"

urlpatterns = [
    path('', views.index, name='index'),
    path('vibor/', views.vibor, name='vibor'),
    path('testing/<slug:t_slug>/', views.testing, name='testing'),
    path('answer/', views.answer, name='answer'),
    path('answer2/', views.answer2, name='answer2'),

    path('file_pdf/<int:ind_id>/', views.file_pdf, name='file_pdf'),
]