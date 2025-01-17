from django.shortcuts import render
from .models import LanguageModel
from .forms import TranslateForm
import requests
from gtts import gTTS
import gtts

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
            langs_available = [x for x in gtts.tts.tts_langs()]

            inp_lang_code=response[0]['detectedLanguage']['language']
            inp_l=LanguageModel.objects.get(Code=inp_lang_code)
            if inp_lang_code in langs_available and inp_lang_code not in ['hy','mk','cy']:
                myobj = gTTS(text=inp, lang=inp_lang_code, slow=False)
                myobj.save('translate/static/inp.mp3')
                inp_speech_available=True
            else:
                inp_speech_available=False
            
            if lang_code in langs_available and lang_code not in ['hy','mk','cy']:
                myobj = gTTS(text=response[0]['translations'][0]['text'], lang=lang_code, slow=False)
                myobj.save('translate/static/response.mp3')
                resp_speech_available=True
            else:
                resp_speech_available=False
            
            

            return render(request, 'translate/result.html', {'inp': inp,'inp_l':inp_l, 'response': response[0]['translations'][0]['text'],'sl':sl,'resp_speech_available':resp_speech_available,'inp_speech_available':inp_speech_available})
    else:
        form = TranslateForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'translate/home.html', {'form': form, 'submitted': submitted})
