from django import forms
from .models import Document
 
# class DocumentForm(forms.ModelForm):
#     class Meta:
#         model = Document
#         fields = ( 'csv_file', ) 

class DocumentForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField() 