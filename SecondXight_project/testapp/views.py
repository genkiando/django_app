from django.http import HttpResponse
from django.template import loader
from .models import Question
from django.core.files.storage import FileSystemStorage

from django.shortcuts import render,redirect
from .forms import DocumentForm,SampleChoiceForm

import pandas as pd
import os
import numpy as np


def index(request):

    template = loader.get_template('testapp/index.html')
    test_text = "アップロードされました"
    context = {
        'test_text': test_text,
    }
    return HttpResponse(template.render(context, request))


 
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


# ----- 1つのファイルを読み込んでアップロード(モデルは使わない) -----

# def model_form_upload(request):
#     if request.method == 'POST':                            
#         form = DocumentForm(request.POST, request.FILES) 

#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])                                 
#             file_obj = request.FILES["file"]
#             file_path = 'uploadfile/file/' + file_obj.name
#             df = pd.read_csv(file_path,encoding="SHIFT-JIS")
#             df_ = df.head(10)
            
#             df_index = list(range(len(df_)))
#             df_columns = list(range(len(df_.columns)))


#             df_ls = df_.values.tolist()
#             table = df_.to_html()
#             print(df_index)
#             print(df_columns)
#             print(request.POST)
            
#             test_text = "アップロードされました"
#             context = {
#               'test_text': test_text,
#               'file_path': file_path,
#               'df': table,
#               'df_ls': df_ls,
#               'df_index': df_index,
#               'df_columns': df_columns,
#               'file_obj': file_obj,
#             }
#             return render(request, 'testapp/index.html', context)                       
#     else:
#         form = DocumentForm()   
#     return render(request, 'testapp/index.html', {
#         'form': form,
#     })

# ----- 複数のファイルをアップロード（モデルは使わない）-----
def model_form_upload(request):
    if request.method == 'POST':                            
        form = DocumentForm(request.POST, request.FILES) 

        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])

            li_df = []  
            # mydict = {} #for文で表作成するとき
            # k = 0       #for文で表作成するとき

            for f in request.FILES.getlist('file'):
                # k = k+1      #for文で表作成するとき
                # columns = [] #for文で表作成するとき
                # total = []   #for文で表作成するとき
                # li_ls = []   #for文で表作成するとき
                file_path = 'uploadfile/file/' + f.name
                df = pd.read_csv(file_path,encoding="SHIFT-JIS")
                df_ = df.head(10)
                table = df_.to_html()
                li_df.append(table) 

                # li_ls.append(df_.values.tolist())                 #dfを多次元配列に変換してリスト化 
                # columns.append(df_.columns.values.tolist())       #カラムを抽出してリスト化
                # total.append(li_ls)                               #for文で表作成するとき
                # total.append(columns)                             #for文で表作成するとき
                # mydict[k]=total                                   #for文で表作成するとき
            
            # form = SampleChoiceForm()

            test_text = "以下のファイルがアップロードされました"
            context = {
              'test_text': test_text,
              'file_path': file_path,
              'li': li_df,
            #   'my_dict':mydict,
            #    'form':form,
            }
            return render(request, 'testapp/index.html', context)                       
    else:
        form = DocumentForm()   
    return render(request, 'testapp/index.html', {
        'form': form,
    })

# -----パス指定するための関数 -----
def handle_uploaded_file(file_obj):
    file_path = 'uploadfile/file/' + file_obj.name 
    with open(file_path, 'wb+') as destination:
        for chunk in file_obj.chunks():
            destination.write(chunk)


def edit(request):
    # print(test_text)
    return render(request, 'testapp/edit.html', {
        # 'form': form,
    })

