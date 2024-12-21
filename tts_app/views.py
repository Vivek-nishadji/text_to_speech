from gtts import gTTS
from django.shortcuts import render
import os

def text_to_speech_view(request):
    if request.method == "POST":
        text = request.POST.get("text", "")

        # Generate audio using gTTS
        audio_file = "static/output_audio.mp3"
        tts = gTTS(text=text, lang='en')
        tts.save(audio_file)

        return render(request, "result.html", {"audio_file": audio_file})

    return render(request, "input.html")