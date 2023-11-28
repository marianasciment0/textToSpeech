from gtts import gTTS
import os
from playsound import playsound

texto = input("Digite aqui o texto: ")
lingua = "pt"

tts = gTTS(texto, lang=lingua)
tts.save("audio.mp3")

playsound("audio.mp3")

# Remova o arquivo de áudio (opcional)
os.remove("audio.mp3")
