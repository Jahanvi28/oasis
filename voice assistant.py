import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak a given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print("You said: " + command)
            return command
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand that.")
            return ""
        except sr.RequestError as e:
            speak("There was an error with the speech recognition service.")
            return ""

# Function to perform actions based on voice commands
def perform_action(command):
    if "hello" in command:
        speak("Hello! How can I help you today?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak("The current time is " + current_time)
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak("Today's date is " + current_date)
    elif "search" in command:
        query = command.replace("search", "").strip()
        search_url = "https://www.google.com/search?q=" + query
        speak("Searching the web for " + query)
        webbrowser.open(search_url)
    elif "exit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't recognize that command.")

# Main loop for continuous listening
while True:
    user_command = listen()
    perform_action(user_command)
