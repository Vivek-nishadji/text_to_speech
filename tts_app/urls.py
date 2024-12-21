from django.urls import path
from .views import text_to_speech_view

urlpatterns = [
    path("", text_to_speech_view, name="tts_input"),
]