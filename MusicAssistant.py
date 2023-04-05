import webbrowser

import speech_recognition as sr

# create a recognizer object
r = sr.Recognizer()

# use the default microphone as the audio source
with sr.Microphone() as source:
    print("Speak something!")
    # listen for audio and convert it to text
    audio = r.listen(source)

try:
    # recognize speech using Google Speech Recognition
    text = r.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))



try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 
var1= text
# to search
query = "youtube"+ var1

list = []
 
for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    #print(j)
    list.append(j)
url=list[0]

firefox = webbrowser.Mozilla("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
firefox.open(url)
