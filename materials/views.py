from django.shortcuts import render, redirect
import subprocess
from django.urls import reverse
from materials.forms import UploadFileForm
from django.http import HttpResponse
from .models import UploadedFile
from .forms import UploadFileForm

# def file_pdf(request):
#     path = 'C:/Users/Fomenko.SM/EXAM_PSO3/Exam/media/uploads/паспорт__КМС_100-80-180_зав_0293_Электромаш_GOLkTwi.pdf'
#     start_pdf=subprocess.Popen([path], shell=True)
#     return redirect(reverse("plumber:index"))
    #return render(request, 'materials/file_pdf.html', {'start_pdf':start_pdf, 'upfile':upfile})

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('materials:upload_file'))
    else:
        form = UploadFileForm()
        files = UploadedFile.objects.all()
        return render(request, 'materials/upload_file.html', {'form': form, 'files': files})
    
def download_file(request, file_id):
    uploaded_file = UploadedFile.objects.get(id=file_id)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response
