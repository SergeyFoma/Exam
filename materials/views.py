from django.shortcuts import render, redirect
import subprocess
from django.urls import reverse
from materials.forms import UploadFileForm
from django.http import HttpResponse
from .models import UploadedFile
from .forms import UploadFileForm

def file_pdf(request):
    path = 'C:/Users/Admin/EXAM/Exam/plumber/static/files_pdf/Информ. письмо ПО (виз.).pdf'
    start_pdf=subprocess.Popen([path], shell=True)
    #return render(request, 'materials/file_pdf.html', {'start_pdf':start_pdf})
    #return start_pdf
    return redirect(reverse("plumber:index"))

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('materials:upload_file')
    else:
        form = UploadFileForm()
        files = UploadedFile.objects.all()
        return render(request, 'materials/upload_file.html', {'form': form, 'files': files})
    
def download_file(request, file_id):
    uploaded_file = UploadedFile.objects.get(id=file_id)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response
