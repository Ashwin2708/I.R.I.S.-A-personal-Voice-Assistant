import datetime
import speak
import webbrowser
import weather
import os


def Action(send) :   
  
    data_btn  = send.lower()

    if "what is your name" in  data_btn or "tell me your name" in data_btn:
      speak.speak("hello, my name is IRIS, I am your personal virtual voice assistant,  made completely open source.")  
      return "hello, my name is IRIS, I am your personal virtual voice assistant,  made completely open source."

    elif "hello" in data_btn  or "hye" in data_btn  or "hay" in data_btn or "Hi" in data_btn: 
        speak.speak("Hello there, How i assist you today!")  
        return "Hello there, How i assist you today!"

    elif "how are you" in  data_btn or "How have you been IRIS?" in data_btn:
            speak.speak("It's a lovely day and I am doing great, what about you?") 
            return "It's a lovely day and I am doing great, what about you?"

    elif "thank you" in data_btn or "thanks" in data_btn:
           speak.speak("its my pleasure to stay with you")
           return "its my pleasure to stay with you"      

    elif "good morning" in data_btn:
           speak.speak("Good morning, i think you might need some help")
           return "Good morning, i think you might need some help"   

    elif "time now" in data_btn or "What is the time right now" in data_btn or "Tell me the time" in data_btn:
          current_time = datetime.datetime.now()
          Time = (str)(current_time.hour)+ " Hour : ", (str)(current_time.minute) + " Minute" 
          speak.speak(Time)
          return str(Time) 

    elif "you can shutdown" in data_btn or "quit the app" in data_btn or "You can rest now" in data_btn or "Bye IRIS" in data_btn:
            speak.speak("ok sir")
            return "ok sir"  

    elif "play some music for me" in data_btn or " play a song" in data_btn or " play music for me" in data_btn or "music" in data_btn:
        webbrowser.open("https://music.youtube.com/watch?v=BlZjTxPAmKc&si=ZvZT3Vf0ZMvguSKY")   
        speak.speak("Here's a song for you, it's quite trending right now!")                   
        return "Here's a song for you, it's quite trending right now!"


    elif 'open google' in data_btn or 'google' in data_btn or "open up gogle for me" in data_btn:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        speak.speak("google open")  
        return "google open"

    elif 'youtube' in data_btn or "open youtube" in  data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        speak.speak("YouTube open") 
        return "YouTube open"    
    
    elif 'play another song' in data_btn or 'play another music' in data_btn :
        url = 'https://google.com/'
        webbrowser.open("https://music.youtube.com/playlist?list=OLAK5uy_l1WlN72z071kMm9HqDce9VyX85ZuSjBr4")
        speak.speak("Playing another music for you")  
        return "Playing another music for you"
    
    elif 'weather' in data_btn :
       ans   = weather.Weather()
       speak.speak(ans) 
       return ans

    elif 'music from my laptop' in data_btn:
        url = 'D:\\music' 
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        speak.speak("songs playing...")
        return "songs playing..." 

    else :
        speak.speak( "i'm able to understand!")
        return "i'm able to understand!"       

