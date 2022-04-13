from django import forms

class TranslateForm(forms.Form):
    input_text=forms.CharField(label='', max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Input'}))
    lang=forms.CharField(label='', max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Language Code'}))
    # l=forms.MultipleChoiceField(label='Choose')
    def __init__(self, *args, **kwargs):
        super(TranslateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    