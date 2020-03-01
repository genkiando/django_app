from django.http import HttpResponse
from django.template import loader
from .models import Question
from django.core.files.storage import FileSystemStorage

from django.shortcuts import render,redirect
from .forms import DocumentForm
from .models import Document


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

 
def model_form_upload(request):
    if request.method == 'POST':                            
        form = DocumentForm(request.POST, request.FILES) 
        if form.is_valid():                                 
            form.save()
            return redirect('index')                        
    else:
        form = DocumentForm()
    return render(request, 'testapp/index.html', {
        'form': form
    })