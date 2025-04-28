from django.urls import path
from . import views

app_name='materials'

urlpatterns=[
    path('file_pdf/', views.file_pdf, name='file_pdf'),
    path('upload/', views.upload_file, name='upload_file'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
]

