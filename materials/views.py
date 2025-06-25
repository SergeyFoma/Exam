from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from materials.forms import UploadFileForm
from django.http import HttpResponse, Http404
from .models import UploadedFile, CategoryMaterials
from .forms import UploadFileForm

from django.http import FileResponse
import os
import subprocess
from exam import settings


c_id=int()
def category_post(request, cat_id):
    cat_post=get_object_or_404(CategoryMaterials, id=cat_id)
    # print('cat_id===',cat_id)
    # print(cat_post)
    global c_id
    c_id=cat_id
        
    context = {
        'cat_post':cat_post,
    }
    return render(request, "materials/category_post.html", context)

def file_pdf(request, ind_id):
    
    pfu=get_object_or_404(UploadedFile,id=ind_id)
    st=str(pfu.file)
    path1=str(settings.MEDIA_ROOT)
    path2='uploads'
    pf=os.listdir(path1+'/'+path2)
    for i in pf:
        if path2+'/'+i == st:
            start_pdf=subprocess.Popen([path1+'/'+path2+'/'+i], shell=True)
            #return redirect(reverse("plumber:index"))
            return redirect(reverse('materials:category_post', kwargs={'cat_id':c_id}))

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



