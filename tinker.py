import speech_recognition as sr#pip install Speech Recognition
import os
import win32com.client
import pyaudio
import webbrowser
import wikipedia#pip install wikipedia
import openai
import datetime
import random
from config  import apikey
#to start working with API you need an API key
speaker=win32com.client.Dispatch('SAPI.SpVoice')
def speak(text):
    '''
    this function will program your chatbot to speak somethong
    '''
    speaker.Speak(text)
def ai(prompt):
  openai.api_key = apikey
  text=f"OpenAI response for prompt:{prompt}\n*******************\n\n"
  response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
  try:
   print(response["choices"][0]["text"])
   text+=response["choices"][0]["text"]
   if not os.path.exists("D:\Openai"):  
      os.mkdir("Openai")
   with open(f"Openai/{prompt[15:30]}.txt","w") as f:#for file name, we are taking first 30 characters of the prompt as the file name
      f.write(text)
   
  except Exception as e:
    print("sorry from LULU") 
def wishMe():
     '''
#     wish according to the system time
     '''
     hour=int(datetime.datetime.now().hour) #you will get the hours ranging from 0-24
     if hour>=0 and hour<12:
      speak("Good Morning!")
     elif hour>=12 and hour<=15:
      speak("Good Afternoon!!")
     else:
      speak("Good Evening!")
chatstr=""
def chat(query,chatstr):#to create a chat
  print(chatstr)
  openai.api_key=apikey
  chatstr+=f"Uer said:{query}\n Lulu: "
  response = openai.Completion.create(
  model="text-davinci-003",
  prompt=chatstr,
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
  print(response["choices"][0]["text"])
  speak(response["choices"][0]["text"])
  chatstr+=f"{response['choices'][0]['text']}\n"
  return response["choices"][0]["text"]
  


  
def takeCommand():
  '''
  It takes microphone input from the user and returns string output
   '''
  r=sr.Recognizer()#Recognizer is a class
  with sr.Microphone() as source:#source microphone
   print("Listening.....")
#    r.pause_threshold=1#seconds of non-speaking audio before a phase is considered complete
   audio=r.listen(source)#listening
  try:
     print("Recognizing....")
     query=r.recognize_google(audio,language='en-in')
     print(f"User said: {query}\n")
  except Exception as e:
    # print(e)
    print("Sorry...from Lulu due to technical glitch unable to recognize")
    return "None"
  return query
if __name__=="__main__":
  wishMe()
  speak("howdy doody! Lulu at your service ....I am here to assist you, how can I be of help?")
  while True:
   query=takeCommand().lower()
   sites=[["youtube","youtube.com"],["google","google.com"],["wikipedia","wikipedia.com"],["geeks for geeks","GeeksforGeeks.org"]]
#logic for executing task based on query
   if 'from wikipedia' in query:
     speak('Lulu at your command')
     query=query.replace("wikipedia","")
     results=wikipedia.summary(query,sentences=3)
     speak("According to wikipedia")
     print(results)
     speak(results)
  
   elif 'open' in query: 
     for site in sites:
      if f"{site[0]}" in query:
       speak(f"okay...opening{site[0]}")
       webbrowser.open(site[1])
   elif 'play music' in query:
     speak('okay...opening music')
     musicpath="C:/Users/Gyanvi/Downloads/Night-Changes(PaglaSongs).mp3"
     os.startfile(musicpath)
   elif 'time' in query:
    Time=datetime.datetime.now().strftime("%H:%M:%S")#returns time in hours minutes and seconds
    speak(f"The time is {Time}")
   elif 'love' or 'smart':
     speak(f"Yeah....I am smart ..ab itna bhi kuch khaas nhi hun.... but don't head over heels for me...")
    
   elif 'artificial intelligence' in query:
      ai(prompt=query)
   else:
      chat(query,chatstr)