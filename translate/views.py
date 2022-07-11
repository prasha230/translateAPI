from django.shortcuts import redirect, render
from .models import LanguageModel
from .forms import TranslateForm
import requests
from gtts import gTTS
import gtts
import os

# Create your views here.
def home(request):
    submitted = False
    if request.method == 'POST':
        form = TranslateForm(request.POST)
        if form.is_valid():
            inp = form.cleaned_data['inp_text']
            sl = form.cleaned_data['lang']
            lang_code = LanguageModel.objects.all().filter(Language=sl).values('Code')[0]['Code']

            # api
            url = "https://microsoft-translator-text.p.rapidapi.com/translate"
            querystring = {"to": lang_code, "api-version": "3.0",
                           "profanityAction": "NoAction", "textType": "plain"}
            payload = [{"Text": inp}]
            headers = {
                "content-type": "application/json",
                "X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com",
                "X-RapidAPI-Key": "0a13a46b22mshff6228808313caep1db3e6jsndf0028c96919"
            }
            response = requests.request("POST", url, json=payload, headers=headers, params=querystring).json()
            
            #making audio files
            myobj = gTTS(text=inp, lang='en', slow=False)  
            os.remove('translate/static/inp.mp3')
            myobj.save('translate/static/inp.mp3')
            
            langs_available = [x for x in gtts.tts.tts_langs()];
            if lang_code in langs_available and lang_code not in ['hy','mk','cy']:
                myobj = gTTS(text=response[0]['translations'][0]['text'], lang=lang_code, slow=False)
                os.remove('translate/static/response.mp3')
                myobj.save('translate/static/response.mp3')
                speech_available=True
            else:
                speech_available=False
            
            

            return render(request, 'translate/result.html', {'inp': inp, 'response': response[0]['translations'][0]['text'],'sl':sl,'speech_available':speech_available})
    else:
        form = TranslateForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'translate/home.html', {'form': form, 'submitted': submitted})
