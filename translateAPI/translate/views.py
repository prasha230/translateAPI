from django.shortcuts import render
from .forms import TranslateForm
from django.http import HttpResponseRedirect
import requests

# Create your views here.
def home(request):
    submitted=False
    if request.method == 'POST':
        form = TranslateForm(request.POST)
        url = "https://microsoft-translator-text.p.rapidapi.com/translate"
        inp=request.POST.get('input_text')
        l=request.POST.get('lang')
        if(inp=='' or l==''): return render(request,'translate/error.html',{})
        querystring = {"to":l,"api-version":"3.0","profanityAction":"NoAction","textType":"plain"}
        payload = [{"Text": inp}]
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com",
            "X-RapidAPI-Key": "0a13a46b22mshff6228808313caep1db3e6jsndf0028c96919"
        }
        response = requests.request("POST", url, json=payload, headers=headers, params=querystring).json()
        return render(request,'translate/result.html',{'inp':inp,'response':response[0]['translations'][0]['text']})
    else:
        form = TranslateForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'translate/home.html',{'form':form,'submitted':submitted})
    

