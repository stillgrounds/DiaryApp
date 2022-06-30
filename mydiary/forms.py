from django import forms
from . models import Diary

class updateform(forms.ModelForm):
    class Meta:
        model = Diary
        fields = '__all__' # single information (firstname, lastname)
        widgets = {
            'text':forms.Textarea(attrs={'class':'form-control'})
        }