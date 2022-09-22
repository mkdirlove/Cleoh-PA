import speech_recognition as sr
import playsound 
from gtts import gTTS, tts
import random
import webbrowser
from datetime import datetime
import pyttsx3
import os

class Cleoh():
    def __init__(self, assist_name, person):
        self.person = person
        self.assit_name = assist_name

        self.engine = pyttsx3.init()
        self.r = sr.Recognizer()
        
        self.voice_data = ''

    def engine_speak(self, text):
        text = str(text)
        self.engine.say(text)
        self.engine.runAndWait()

    def record_audio(self, ask=""):


        with sr.Microphone() as source:
            if ask:
                print('Recording...')
                self.engine_speak(ask)

            audio = self.r.listen(source,5 , 5)
            print('Looking at my database...')
            try:
                self.voice_data = self.r.recognize_google(audio)

            except sr.UnknownValueError:
                self.engine_speak('Sorry master, I did not get what you said. Can you please repeat?')

            except sr.RequestError:
                self.engine_speak('Sorry master, my server is down :(')

            print("~> ",self.voice_data.lower())
            self.voice_data = self.voice_data.lower()

            return self.voice_data.lower()

    def engine_speak(self, audio_strig):
        audio_strig = str(audio_strig)
        tts = gTTS(text=audio_strig, lang='en')
        r = random.randint(1,20000)
        audio_file = 'audio' + str(r) + '.mp3'
        tts.save(audio_file)
        playsound.playsound(audio_file)
        print(self.assit_name + ':', audio_strig)
        os.remove(audio_file)


    def there_exist(self, terms):
        for term in terms:
            if term in self.voice_data:
                return True


    def respond(self, voice_data):
        if self.there_exist(['hey', 'hi', 'hello', 'oi', 'kumusta', 'hoy', 'wake up', 'boot up']):
            greetigns = [f'Hi sir {self.person}, what are we doing today?',
                        'Hi master, how can I help you?',
                        'Hi master, what do you need?',
                        'Hi master, what can I do for you?',
                        'Hi master, kumusta ka?',
                        'Hi master, anong maitutulong ko?']

            greet = greetigns[random.randint(0,len(greetigns)-1)]
            self.engine_speak(greet)

        #google
        if self.there_exist(['search for']) and 'youtube' not in voice_data:
            search_term = voice_data.split("for")[-1]
            url =  "http://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            self.engine_speak("Here is what I found for " + search_term + 'on google')

        #google 
        if self.there_exist(["search youtube for"]):
            search_term  = voice_data.split("for")[-1]
            url = "http://www.youtube.com/results?search_query=" + search_term
            webbrowser.get().open(url)
            self.engine_speak("Here is what i found for" + search_term + 'on youtube')

        #gmail
        if self.there_exist(['open gmail']):
            url = "gmail.com"
            webbrowser.get().open(url)
            self.engine_speak("Your gmail is now open sir.")

        #facebook
        if self.there_exist(['open facebook']):
            url = "facebook.com/mkdirlove.dph"
            webbrowser.get().open(url)
            self.engine_speak("Your facebook is now open sir.")

        #classroom
        if self.there_exist(['open classroom']):
            url = "classroom.google.com"
            webbrowser.get().open(url)
            self.engine_speak("Your google classroom is now open sir.")

        #github
        if self.there_exist(['open github']):
            url = "github.com/mkdirlove"
            webbrowser.get().open(url)
            self.engine_speak("Your github is now open sir.")

        #cxsecurity
        if self.there_exist(['open cx']):
            url = "https://cxsecurity.com/author/MR.%24UD0/1/"
            webbrowser.get().open(url)
            self.engine_speak("Your cxsecurity is now open sir.")

        #musiic
        if self.there_exist(['music please']):
            url = "https://www.youtube.com/watch?v=ZyS5q9m0T_c&list=RDGMEMQ1dJ7wXfLlqCjwV0xfSNbAVMZyS5q9m0T_c&start_radio=1"
            webbrowser.get().open(url)
            self.engine_speak("Enjoy the music sir.")
                                
        #reboot
        if self.there_exist(['reboot']):
            self.engine_speak("Your computer will reboot now.")
            os.system("reboot")

        #reboot
        if self.there_exist(['shutdown']):
            self.engine_speak("Your computer will shutdown now.")
            os.system("shutdown 0")
                    
        #time
        if self.there_exist(['time check']):
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            engine = pyttsx3.init()
            self.engine_speak(f"The time is {current_time}")

pa = Cleoh('Cleoh', 'sudo')

while True:
    voice_data = pa.record_audio('Listening...')
    pa.respond(voice_data)

    if pa.there_exist(['bye', 'goodbye', 'seeyou', 'see you later', 'see you']):
        pa.engine_speak("Have a nice day master! Good bye!")
        break
