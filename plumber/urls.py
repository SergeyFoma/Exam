from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

app_name="plumber"

urlpatterns = [
    #path('', views.index, name='index'),
    path('',cache_page(30)(views.Index.as_view()), name='index'),
    path('vibor/', views.vibor, name='vibor'),
    path('testing/<slug:t_slug>/', views.testing, name='testing'),
    path('answer/', views.answer, name='answer'),
    path('answer2/', views.answer2, name='answer2'),
    path("parser/", views.parser, name='parser'),
    path('result/',views.result,name="result"),
    path("delete_file/<str:name>/",views.delete_file,name="delete_file"),
    #path('download/<str:file_path>/',views.download,name='download'),
    #path('download/<str:filename>/',views.download,name='download'),
    #path('download/',views.download,name='download'),
    

    #path('file_pdf/<int:ind_id>/', views.file_pdf, name='file_pdf'),
]