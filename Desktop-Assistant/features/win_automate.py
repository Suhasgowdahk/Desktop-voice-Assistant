import keyboard
from features.sense import speak
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
from bs4 import BeautifulSoup
import webbrowser
import pywhatkit as wk
import os
import cv2
import pyautogui as pi
import time
import operator
import requests
import sys
import random
#--------------------- Automating Windows -----------------
def WindowAutomate(query):
    #for closing the tab
    if 'close this tab' in query:
        keyboard.press_and_release('ctrl + w')
        speak('Closed.')
        return 1
        
    #to open new tab
    elif 'open new tab' in query:
        keyboard.press_and_release('ctrl + t')
        speak('Opened a new tab.')
        return 1
        
    #to open new window
    elif 'open new window' in query:
        keyboard.press_and_release('ctrl + n')
        speak('Opened a new window.')
        return 1
        
    #to open history
    elif 'browsing history' in query:
        keyboard.press_and_release('ctrl + h')
        speak('Opened browsing history.')
        return 1
        
    #to open downloads
    elif 'open download' in query:
        keyboard.press_and_release('ctrl + j')
        speak('Opened')
        return 1
        
    #to open next page
    elif 'next page' in query or 'go next' in query:
        keyboard.press_and_release('Alt + Right arrow')
        speak('Moved to next page.')
        return 1
        
    #to open prev page
    elif 'previous page' in query or 'go back' in query:
        keyboard.press_and_release('Alt + Left arrow')
        speak('Moved back to previous page.')
        return 1
        
    elif 'show desktop' in query or 'maximize all' in query or 'minimise all' in query:
        keyboard.press_and_release('Windows + d')
        speak("Done sir!")
        return 1

    #minimize window
    elif 'minimise' in query:
        keyboard.press_and_release('Alt + space + n')
        speak('Minimized window')
        return 1
    elif 'open incognito window' in query:
        pi.hotkey('ctrl', 'shift', 'n')
        return 1
    elif "open file" in query:
        keyboard.press_and_release("Windows + e")
        speak("Opened Files Explorer.")
        return 1

    elif 'close window' in query:
        keyboard.press_and_release('Alt + f4')
        speak("Closed.")
        return 1

    elif 'show notification' in query or 'open notification' in query or 'close notification' in query:
        keyboard.press_and_release('Windows + a')
        speak('Done Sir!')
        return 1

    elif 'stop the video' in query:
        keyboard.press_and_release("Space")
        return 1
    
    elif 'open youtube' in query:
        from features.sense import takecomand
        speak("what will you like to watch ?")
        qrry=takecomand().lower()
        wk.playonyt(f"{qrry}")
        return 1
    
    elif 'play movie' in query:
        npath = r"C:\\Users\\Suhas HK\\Downloads\\Telegram Desktop\\movie.mkv" 
        os.startfile(npath)  
        return 1
    elif 'close movie' in query:
        os.system("taskkill /f /im vlc.exe") 
        return 1       
    elif 'search on youtube' in query:
        query=query.replace("search on youtube","")
        ebbrowser.open(f"www.youtube.com/results?search_query={query}")
        return 1
    #type with voice
    elif query == 'type my command':
        from features.sense import takecomand
        note = None
        speak("What should i write? ")
        while note != 'stop writing':
            note = takecomand()
            keyboard.write(note + '.', delay=0.1)
        return 1
    elif "open camera" in query:
        cap=cv2.VideoCapture(0)
        while True:
            ret,img=cap.read()
            cv2.imshow('webcam',img)
            k=cv2.waitKey(50)
            if k==27:
                break;
        cap.release()
        cv2.destroyAllWindows()
        return 1
    elif "close camera" in query:
        pi.press('esc')
    else:
        return 0