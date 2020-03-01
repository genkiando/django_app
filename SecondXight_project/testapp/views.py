from django.http import HttpResponse
from django.template import loader
from .models import Question, Document
from django.core.files.storage import FileSystemStorage

from django.shortcuts import render,redirect
from .forms import DocumentForm

import pandas as pd
import os
# import numpy as np


def index(request):

    template = loader.get_template('testapp/index.html')
    test_text = "アップロードされました"
    context = {
        'test_text': test_text,
    }
    return HttpResponse(template.render(context, request))


# def result(request, result_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % result_id)

 
# def model_form_upload(request):
#     if request.method == 'POST':                            
#         form = DocumentForm(request.POST, request.FILES) 
#         if form.is_valid():                                 
#             form.save()
#             return redirect('index')                        
#     else:
#         form = DocumentForm()
    
#     return render(request, 'testapp/index.html', {
#         'form': form,
#     })



def model_form_upload(request):
    if request.method == 'POST':                            
        form = DocumentForm(request.POST, request.FILES) 

        if form.is_valid():                                 
            file_obj = request.FILES["file"]
            file_path = 'uploadfile/file/' + file_obj.name
            df = pd.read_csv(file_path,encoding="SHIFT-JIS")
            df_ = df.head()
            table = df_.to_html()
            print(df_)
            
            test_text = "アップロードされました"
            context = {
              'test_text': test_text,
              'file_path': file_path,
              'df': table,
              'file_obj': file_obj,
            }
            return render(request, 'testapp/index.html', context)                       
    else:
        form = DocumentForm()   
    return render(request, 'testapp/index.html', {
        'form': form,
    })



# def handle_uploaded_file(f):
#     with open('some/file/name.txt', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)