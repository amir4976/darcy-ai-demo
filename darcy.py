import speech_recognition as SR
import pyaudio
from playsound import playsound
from datetime import datetime
from gtts import gTTS
import os
import ctypes
import subprocess
import pyfiglet
import sys
import importlib
import pyautogui

# flag to show its woman voice or man voice
voice_flag =False
# if this is change voice is change
target_voice = 'files'

#it run every time you say change voice
def changeMode():
    global target_voice
    if(voice_flag == False):
        target_voice =  'files'   
    else:   
        target_voice = 'jarvis'

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

# make a fancy header
result = pyfiglet.figlet_format("DARCY", font = "colossal" )
print(bcolors.WARNING + result)



i = 0
while i < 1000:
    #get time 
    h = datetime.now().hour
    m = datetime.now().minute

    #make it sound
    audioH = gTTS(text=str(h), lang="en", slow=False)
    audioM = gTTS(text=str(m), lang="en", slow=False)

    #save it
    audioH.save(f"./{target_voice}/h.mp3")
    audioM.save(f"./{target_voice}/M.mp3")



    rec = SR.Recognizer()
    mic = SR.Microphone()

    #make a function for play for better performance
    def play(target):
        playsound(target);

    # get string and show if is in there a number 
    def num_there(s):
        return any(i.isdigit() for i in s)
    




    print ('time and introduce and chat and thanks and browser and download manger... this is just a demo')


    #use speech recognition
    with mic as source:
        print('ready...')
        rec.adjust_for_ambient_noise(source,duration=1)

        audio = rec.listen(source=source)
        try:
            # make audio to text 
            text = rec.recognize_google(audio)

            # for conversation
            if 'Darcy are you there' in text or text == 'Darcy dude are you there' or text == 'Darcy body are you there' or text == 'good morning Darcy' or text == 'hello' or text == 'hello Darcy' or text == 'Darcy':
                play(f'./{target_voice}/at-your-service-sir.mp3')
                play(f'./{target_voice}/online-and-ready.mp3')
                


            # for get time
            if ('time' in text):
                play(f'./{target_voice}/yes-sir-time-is.mp3')
                play(f'./{target_voice}/h.mp3') 

                play(f'./{target_voice}/and.mp3')

                play(f'./{target_voice}/M.mp3')
                play(f'./{target_voice}/clock.mp3')



            # for introduce
            if ('introduce' in text or text == 'who are you' or text == 'who is this'):
                play(f'./{target_voice}/yes sir my name is..mp3')
            
            
            # for thanks
            if ('thank you' in text):
                play(f'./{target_voice}/always-sir.mp3')
            # for make systems online
            
            
            
            if ('online' in text):
                play(f'./{target_voice}/access-denied-password-requested.mp3')
                systemPassword = input('plase enter password... : ')

                if systemPassword == 'for dark side':
                    play(f'./{target_voice}/access-success.mp3')
                    subprocess.call(
                        ['C:\Program Files\Microsoft VS Code\\Code.exe'])
                else:
                    play(f'./{target_voice}/access-denied.mp3')
          
          
          
           #for lock computer
            if ('lock' in text):
                play(f'./{target_voice}/very-well-sir.mp3')
                # lock pc with ctypes package
                ctypes.windll.user32.LockWorkStation()
           
           
           
            # for shot down        
            if 'shut down' in text:
                play(f'./{target_voice}/system-is-shutting-down (1).mp3')
                #shutdown pc with os system 
                os.system("shutdown /s /t 1")
           
           
            # for browser command
            if 'browser' in text:
                play(f'./{target_voice}/very-well-sir.mp3')
                # run download manger with subProcess package
                subprocess.call(
                    ['C:\Program Files (x86)\Microsoft\Edge\Application\\msedge.exe'])
           
           
            # for this PC commend
            if 'PC' in text:
                play(f'./{target_voice}/very-well-sir.mp3')
                # run this pc with subProcess package
                subprocess.run(["explorer", ","])
           
           
            # for download manger
            if 'download manager' in text:
                play(f'./{target_voice}/very-well-sir.mp3')
                subprocess.call(['C:\Program Files (x86)\Internet Download Manager\\IDMan.exe'])
           
           
           
            #for move mouse to position it get two number in input and you have to say {'kama' = ,} between them 
            if num_there(text):
                play(f'./{target_voice}/very-well-sir.mp3')
                main_text = text
                Array_Main_Text = list(map(str.strip, text.split(',')))
                print(Array_Main_Text[1])
                pyautogui.moveTo(int(Array_Main_Text[0]) , int(Array_Main_Text[1]) , duration=0.5)

          
          
          
            # for click
            if 'select' in text:
                pyautogui.doubleClick()

          
          
          
            # for type something in text inputs or some apps you have to sey type in start of your text  
            if 'type' in text :
                newText = text.replace("type","")
                pyautogui.write(newText) 

           
           
           
            # for change voice from male to female and upside
            if 'change voice'  in text :
                play(f'./{target_voice}/very-well-sir.mp3')
                if(voice_flag == False):
                    voice_flag= True
                    changeMode()
                else:
                    voice_flag = False
                    changeMode()
              
                     

        # and for error handling
        except:
           print('system is dont understand')
        finally:
            i += 1
    
    
    