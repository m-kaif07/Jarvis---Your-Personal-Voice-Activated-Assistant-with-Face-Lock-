import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import send_email
from lock import face_lock

# Initializing Engine and Voices variables
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# ---------- Defining Speak function -----------
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# ---------- Greet GM/GF/GE ------------
def wishMe():
    current_hour = int(datetime.datetime.now().hour)
    if current_hour >= 0 and current_hour < 12:
        speak("Good Morning!")
    elif current_hour >= 12 and current_hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I'm Jarvis, sir. How may I help you?")

# ---------- Taking command from the user-----------
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print("Listening...")
        r.pause_threshold = 0.6
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print("You said: ", query)
        return query
    except Exception as e:
        print(e)
        print("Say that again, please...")
        return "None"

# ----------- search on google -------------
def google_search(search_query):
    search_url = f"https://www.google.com/search?q={search_query}"
    webbrowser.open(search_url)


# Main function
if __name__ == "__main__":

    # Face unlock feature
    speak("Please unlock the program with Face")
    path = 'JARVIS/Kaif.jpg' # provide your image path for authentication
    # path2 = 'JARVIS/Virat01.jpg'
    result = face_lock(path)

    if result:
        print("Program Unlocked !")
    
        wishMe() # to greet the user
        while True:
            query = takeCommand().lower()
            print("You said:", query)  # to print the recognized command
            
            # Perform actions based on the recognized command
            if 'wikipedia' in query: 
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2) 
                speak("According to Wikipedia")
                # print(results)
                speak(results)

            elif "what's the time" in query:
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The current time is {current_time}")

            elif "who are you" in query:
                speak("My name is Jarvis, I'm a virtual-assistant for automating various daily tasks on computer, such as sending email, opening any application, chatting, etc. I have been created by Mohammad Kaif.")

            elif "open google" in query:
                webbrowser.open("quora.com")

            elif "open youtube" in query:
                webbrowser.open("youtube.com")

            elif "github profile" in query:
                webbrowser.open("github.com/m-kaif07")
            
            elif "open quora" in query:
                webbrowser.open("quora.com")
            
            elif "play music" in query:
                music_dir = 'D:\\music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif "open vs code" in query:
                code_path = "C:\\Users\\moham\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(code_path)

            elif "open web dev folder" in query:
                file_path = "C:\\Users\\moham\\OneDrive\\Desktop"
                os.startfile(file_path)

            elif "open notepad" in query:
                notepad_path = "C:\\Windows\\notepad.exe"
                os.startfile(notepad_path)

            elif "send email" in query:
                try:
                    speak("whom I should send the email to? ")
                    recipient_name = takeCommand().lower()
                    speak('what should I send? ')
                    content = takeCommand()
                    send_email.sendEmail(recipient_name, content)
                    speak("Email has been sent!") 
                except Exception as e:
                    print(e)
                    speak("sorry, I'm not able to sent email")

            elif "search on google" in query:
                speak("what should I search for sir?")
                search_query = takeCommand()
                google_search(search_query)

            elif "exit" or "quit" in query:
                speak("Goodbye!")
                exit()

    else:
        speak("Sorry, Your Face does not match. Cannot Unlock The Program.")
        print("Face doesn't match not found. Program still Locked.")
