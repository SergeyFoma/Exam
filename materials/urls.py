from django.urls import path
from . import views

app_name='materials'

urlpatterns=[
    #path('file_pdf/', views.file_pdf, name='file_pdf'),
    path('upload/', views.upload_file, name='upload_file'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
    path('category_post/<int:cat_id>/', views.category_post, name="category_post"),

    path('file_pdf/<int:ind_id>/', views.file_pdf, name='file_pdf'),
]

