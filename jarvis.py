import pyttsx3
def speak(audio):
    import datetime
    pass
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
print(voices[0].id)
engine.say("Hello sir i am jarvis")
engine.runAndWait()
if __name__ == '__main__':
    speak("Hello sir i am jarvis")
engine = speak.__eq__23

        
     
    
    
    
    
    