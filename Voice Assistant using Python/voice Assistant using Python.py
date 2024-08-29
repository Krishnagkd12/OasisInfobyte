import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to voice commands
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}\n")
            return command.lower()
        
        except sr.UnknownValueError:
            print("Sorry, I did not catch that.")
            return ""
        
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return ""

# Main function for the voice assistant
def voice_assistant():
    while True:
        command = listen()
        
        if 'hello' in command:
            speak("Hello! How can I assist you today?")
        
        elif 'what is your name' in command:
            speak("I am your Python voice assistant.")
        
        elif 'exit' in command or 'stop' in command:
            speak("Goodbye!")
            break
        
        else:
            speak("I'm sorry, I didn't understand that command.")

# Run the voice assistant
voice_assistant()