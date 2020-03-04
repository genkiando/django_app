from django import forms
# from .models import Document
 
# class DocumentForm(forms.ModelForm):
#     class Meta:
#         model = Document
#         fields = ( 'csv_file', ) 

# class DocumentForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField() 

class DocumentForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

class SampleChoiceForm(forms.Form):
    choice1 = forms.fields.ChoiceField(
        choices = (
            ('IJ', 'InnerJoin'),
            ('OR', 'OuterJoin/Right'),
            ('OL', 'OuterJoin/Left'),         
        ),
        required=True,
        widget=forms.widgets.Select
    )