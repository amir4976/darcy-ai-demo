import speech_recognition as SR
import pyaudio
from playsound import playsound
import datetime
from gtts import gTTS
import os
import ctypes
import subprocess
import sys
import pyfiglet

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



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

def play(target):
    playsound(target);


result = pyfiglet.figlet_format("darcy", font = "colossal" )
print(bcolors.WARNING + result)



with mic as source:
    print('ready...')
    rec.adjust_for_ambient_noise(source,duration=1)

    audio = rec.listen(source=source)
    try:
        text = rec.recognize_google(audio)
        print(text)
        if text == 'Darcy are you there' or text == 'Darcy dude are you there' or text == 'Darcy body are you there' or text == 'good morning Darcy' or text == 'hello' or text == 'hello Darcy' or text == 'Darcy':
            print('true')
            play('./files/at-your-service-sir.mp3')
            play('./files/online-and-ready.mp3')

        if ('time' in text):
            play('./files/yes-sir-time-is.mp3')
            play('./files/example.mp3')

            play('./files/and.mp3')

            play('./files/exampleM.mp3')
            play('./files/clock.mp3')

        if ('introduce' in text):
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

        if ('lock' in text):
            play('./files/very-well-sir.mp3')
            ctypes.windll.user32.LockWorkStation()
        
        if 'shut down' = text:
            play('./files/system-is-shutting-down (1).mp3')
            # os.system("shutdown /s /t 1")

        if 'browser' in text:
            play('./files/very-well-sir.mp3')
            subprocess.call(
                ['C:\Program Files (x86)\Microsoft\Edge\Application\\msedge.exe'])

        if 'this PC' in text:
            play('./files/very-well-sir.mp3')
            subprocess.run(["explorer", ","])

        if 'download manager' in text:
            play('./files/very-well-sir.mp3')
            subprocess.call(['C:\Program Files (x86)\Internet Download Manager\\IDMan.exe'])

    except:
        print('failed')
        
input('press any key')