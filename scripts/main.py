import win32api
import speech_recognition as sr
import pyttsx3
import pywintypes
import pywhatkit as searcher
import flask
import datetime
import wikipedia as wiki
import pyjokes

assistlisten = sr.Recognizer()
assistspeak = pyttsx3.init()
voices = assistspeak.getProperty('voices')
rate = assistspeak.getProperty('rate')
assistspeak.setProperty('voice',voices[0].id)

def talk(said):
    assistspeak.say(said)
    assistspeak.runAndWait()
talk('I am Newton, Your Virtual Assistant')
talk('What can I do for you?')
def take_command():
    try:
        with sr.Microphone() as source:
            talk('I am Listening')
            print('Listening...')
            voice = assistlisten.listen(source)
            command = assistlisten.recognize_google(voice)
            command=command.lower()
            if 'newton' in command:
                command =command.replace('newton ','')
            print(command)
            talk('You said ' + command)

    except:
        pass
    return command

def run_Newton():
    command=take_command()
    if 'play' in command:
        song = command.replace('play ', '')
        talk('playing ' + song)
        searcher.playonyt(song)
    elif 'time' in command:
        time =datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'wikipedia' in command:
        query = command.replace('wikipedia ', '')
        answer = wiki.summary(query,1)
        print(answer)
        assistspeak.setProperty('rate', 230)
        talk(answer)
        assistspeak.setProperty('rate', 200)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')

while True:
    run_Newton()
