from django.shortcuts import render

from .models import LanguageModel
from .forms import TranslateForm
from django.http import HttpResponseRedirect
import requests

# Create your views here.
def home(request):
    submitted=False
    if request.method == 'POST':
        form = TranslateForm(request.POST)
        if form.is_valid():
            inp=form.cleaned_data['inp_text']
            # lang=form.cleaned_data['lang']
            sl=form.cleaned_data['l']
            lc=LanguageModel.objects.all().filter(Language=sl).values('Code')[0]['Code']
            print(lc)
            url = "https://microsoft-translator-text.p.rapidapi.com/translate"
            querystring = {"to":lc,"api-version":"3.0","profanityAction":"NoAction","textType":"plain"}
            payload = [{"Text": inp}]
            headers = {
                "content-type": "application/json",
                "X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com",
                "X-RapidAPI-Key": "0a13a46b22mshff6228808313caep1db3e6jsndf0028c96919"
            }
            response = requests.request("POST", url, json=payload, headers=headers, params=querystring).json()
            form=TranslateForm
            return render(request,'translate/result.html',{'inp':inp,'response':response[0]['translations'][0]['text']})
    else:
        form = TranslateForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'translate/home.html',{'form':form,'submitted':submitted})
    

