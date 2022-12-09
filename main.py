import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import pywhatkit
import pyjokes


# this method is for taking the commands
# and recognizing the command from the
# speech_Recognition module we will use
# the recognizer method for recognizing
def take_command():
    r = sr.Recognizer()

    # from the speech_Recognition module
    # we will use the Microphone module
    # for listening the command
    with sr.Microphone() as source:
        print('Listening')

        # seconds of non-speaking audio before
        # a phrase is considered complete
        r.pause_threshold = 0.7
        audio = r.listen(source)

        # Now we will be using the try and catch
        # method so that if sound is recognized
        # it is good else we will have exception
        # handling
        try:
            print("Recognizing")

            # for Listening the command in indian
            # english we can also use 'hi-In'
            # for hindi recognizing
            query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", query)

        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"

        return query


def speak(audio):
    engine = pyttsx3.init()
    # getter method(gets the current value
    # of engine property)
    voices = engine.getProperty('voices')

    # setter method .[0]=male voice and
    # [1]=female voice in set Property.
    engine.setProperty('voice', voices[0].id)

    # Method for the speaking of the assistant
    engine.say(audio)

    # Blocks while processing all the currently
    # queued commands
    engine.runAndWait()


def tell_day():
    # This function is for telling the
    # day of the week
    day = datetime.datetime.today().weekday() + 1

    # this line tells us about the number
    # that will help us in telling the day
    day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in day_dict.keys():
        day_of_the_week = day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)


def tell_time():
    # This method will give the time
    time = str(datetime.datetime.now())

    # the time will be displayed like
    # this "2020-06-05 17:50:14.582630"
    # nd then after slicing we can get time
    print(time)
    hour = time[11:13]
    minute = time[14:16]
    speak("The time is sir" + hour + "Hours and" + minute + "Minutes")


def greeting():
    # This function is for when the assistant
    # is called it will say hello and then
    # take query
    speak("hello sir I am your virtual assistant. Tell me how can I help you ")


def take_query():
    # calling the Hello function for
    # making it more interactive
    greeting()

    # This loop is infinite as it will take
    # our queries continuously until and unless
    # we do not say bye to exit or terminate
    # the program
    while True:

        # taking the query and making it into
        # lower case so that most of the time
        # query matches, and we get the perfect
        # output
        query = take_command().lower()
        if "amigo" in query:
            query = query[query.find("amigo") + 5:]

            if "open youtube" in query:
                speak("Opening YouTube ")

                # in the open method we just to give the link
                # of the website, and it automatically opens
                # it in your default browser
                webbrowser.open("www.youtube.com")
                continue

            elif "open google" in query:
                speak("Opening Google ")
                webbrowser.open("www.google.com")
                continue

            elif "open netflix" in query:
                speak("Opening Netflix ")
                webbrowser.open("www.netflix.com")
                continue

            elif "which day it is" in query:
                tell_day()
                continue

            elif "what time is it" in query or "what is the time" in query:
                tell_time()
                continue
            elif 'play' in query:
                song = query.replace('play', '')
                speak('playing ' + song)
                pywhatkit.playonyt(song)

            # this will exit and terminate the program
            elif "bye" in query:
                speak("Bye. don't hesitate don't to ask for my assistance")
                exit()

            elif 'who is' in query:
                person = query.replace('who is', '')
                info = wikipedia.summary(person, 1)
                print(info)
                speak("According to wikipedia")
                speak(info)

            elif 'what is' in query:
                thing = query.replace('what is', '')
                info = wikipedia.summary(thing, 1)
                print(info)
                speak("According to wikipedia")
                speak(info)

            elif "search for" in query:
                # if any one wants to have an information
                # from wikipedia
                speak("Checking the wikipedia ")
                query = query.replace("search for", "")

                # it will give the summary of 4 lines from
                # wikipedia we can increase and decrease
                # it also.
                result = wikipedia.summary(query, sentences=1)
                speak("According to wikipedia")
                speak(result)

            elif 'joke' in query:
                speak(pyjokes.get_joke())

            elif "tell me your name" in query or "what is your name" in query or "what's your name" in query:
                speak("I am Jaafar. Your Genie, sorry I mean your Assistant")

            else:
                speak("Please say the command again, I couldn't understand")


if __name__ == '__main__':
    # main method for executing
    # the functions
    take_query()
