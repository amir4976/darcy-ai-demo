import speech_recognition as SR
import pyaudio
from playsound import playsound
from datetime import datetime
from gtts import gTTS
import os
import ctypes
import subprocess
import sys
import pyfiglet

# text colors 
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


#get time 
h = datetime.now().hour
m = datetime.now().minute

#make it sound
audioH = gTTS(text=str(h), lang="en", slow=False)
audioM = gTTS(text=str(m), lang="en", slow=False)

#save it
audioH.save("./files/h.mp3")
audioM.save("./files/M.mp3")



rec = SR.Recognizer()
mic = SR.Microphone()

#make a function for play for better performance
def play(target):
    playsound(target);



# make a fancy header
result = pyfiglet.figlet_format("darcy", font = "colossal" )
print(bcolors.WARNING + result)


#use speech recognition
with mic as source:
    print('ready...')
    rec.adjust_for_ambient_noise(source,duration=1)

    audio = rec.listen(source=source)
    try:
        text = rec.recognize_google(audio)
        print(text)
        # for conversation
        if 'Darcy are you there' in text or text == 'Darcy dude are you there' or text == 'Darcy body are you there' or text == 'good morning Darcy' or text == 'hello' or text == 'hello Darcy' or text == 'Darcy':
            print('true')
            play('./files/at-your-service-sir.mp3')
            play('./files/online-and-ready.mp3')
        # for get time
        if ('time' in text):
            play('./files/yes-sir-time-is.mp3')
            play('./files/h.mp3')

            play('./files/and.mp3')

            play('./files/M.mp3')
            play('./files/clock.mp3')
        # for introduce
        if ('introduce' in text):
            play('./files/yes sir my name is..mp3')
        # for thanks
        if (text == 'thank you Darcy'):
            play('./files/always-sir.mp3')
        # for make systems online
        if ('online' in text):
            play('./files/access-denied-password-requested.mp3')
            systemPassword = input('plase enter password... : ')

            if systemPassword == 'for dark side':
                play('./files/access-success.mp3')
                subprocess.call(
                    ['C:\Program Files\Microsoft VS Code\\Code.exe'])
            else:
                play('./files/access-denied.mp3')
        #for lock computer
        if ('lock' in text):
            play('./files/very-well-sir.mp3')
            ctypes.windll.user32.LockWorkStation()
        # for shot down        
        if 'shut down' in text:
            play('./files/system-is-shutting-down (1).mp3')
            # os.system("shutdown /s /t 1")
        # for browser command
        if 'browser' in text:
            play('./files/very-well-sir.mp3')
            subprocess.call(
                ['C:\Program Files (x86)\Microsoft\Edge\Application\\msedge.exe'])
        # for this PC commend
        if 'PC' in text:
            play('./files/very-well-sir.mp3')
            subprocess.run(["explorer", ","])
        # for download manger
        if 'download manager' in text:
            play('./files/very-well-sir.mp3')
            subprocess.call(['C:\Program Files (x86)\Internet Download Manager\\IDMan.exe'])
    # and for error handling
    except:
        print('failed')
        
# last line input
input('press enter key ...')