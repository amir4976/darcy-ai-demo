import speech_recognition as SR
import pyaudio
from playsound import playsound
import datetime
from gtts import gTTS
import os
import ctypes
import subprocess

h = datetime.datetime.now().hour
m = datetime.datetime.now().minute

myh = str(h)
mym = str(m)

audioH = gTTS(text=myh, lang="en", slow=False)
audioM = gTTS(text=mym, lang="en", slow=False)

audioH.save("./files/h.mp3")
audioM.save("./files/M.mp3")



rec = SR.Recognizer()
mic = SR.Microphone()
print(SR.Microphone.list_microphone_names())
def play(target):
    playsound(target);


with mic as source:
    print('ready...')
    rec.adjust_for_ambient_noise(source,duration=1)

    audio = rec.listen(source=source)
    try:
        text = rec.recognize_google(audio)
        

        print(text)
        if text == 'Darcy are you there' or text == 'Darcy dude are you there' or text == 'Darcy body are you there' or text == 'good morning Darcy':
            print('true')
            play('./files/at-your-service-sir.mp3')
            play('./files/online-and-ready.mp3')

        if text == 'Darcy can you tell me what time is it':
            play('./files/yes-sir-time-is.mp3')
            play('./files/example.mp3')

            play('./files/and.mp3')

            play('./files/exampleM.mp3')
            play('./files/clock.mp3')

        if (text == 'Darcey please introduce yourself'):
            play('./files/yes sir my name is..mp3')

        if (text == 'thank you Darcy'):
            play('./files/always-sir.mp3')

        if (text == 'Darcy make all systems online'):
            play('./files/access-denied-password-requested.mp3')
            systemPassword = input('plase enter password...')

            if systemPassword == 'for dark side':
                play('./files/access-success.mp3')
                subprocess.call(
                    ['C:\Program Files\Microsoft VS Code\\Code.exe'])
            else:
                play('./files/access-denied.mp3')

        if text == 'Darcy lock my computer':
            play('./files/very-well-sir.mp3')
            ctypes.windll.user32.LockWorkStation()
        
        if text == 'Darcy shut down':
            play('./files/system-is-shutting-down (1).mp3')
            # os.system("shutdown /s /t 1")

        if text == 'Darcy open browser':
            play('./files/very-well-sir.mp3')
            subprocess.call(
                ['C:\Program Files (x86)\Microsoft\Edge\Application\\msedge.exe'])

        if text == 'Darcy open this PC':
            play('./files/very-well-sir.mp3')
            subprocess.run(["explorer", ","])

        if text == 'Darcy open download manager':
            play('./files/very-well-sir.mp3')
            subprocess.call(['C:\Program Files (x86)\Internet Download Manager\\IDMan.exe'])

    except:
        print('failed')
