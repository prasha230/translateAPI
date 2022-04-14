from cProfile import label
from django import forms

from .models import LanguageModel

class TranslateForm(forms.Form):
    inp_text=forms.CharField(label='', max_length=100,widget=forms.Textarea(attrs={'placeholder': 'Input','class':'form-control','rows':5,'columns':15}))
    # lang=forms.CharField(label='', max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Language Code'}))
    l=forms.ModelChoiceField(label='',queryset=LanguageModel.objects.all(),empty_label="Select Language",widget=forms.Select(attrs={'class':'form-select'}))
    