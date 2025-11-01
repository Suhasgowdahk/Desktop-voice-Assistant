#---------------------------------For Features----------------------------------------
import pyautogui
from features.basic import *
from features import walter
from features.sense import *
import os
import sys
from features.search_web import findAns
from features.win_automate import WindowAutomate
#---------------------------------For GUI -------------------------------------------
import PyQt5
from PyQt5.QtCore import QTime, QTimer, QDate, Qt
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from Walter_UI import Ui_Walter
#-----------------------------------------------------------------------------------
import pyjokes #for jokes
#-----------------------------------------------------------------------------------

class MainThread(QThread):
    def __init__(self) -> None:
        self.x = 1
        super(MainThread, self).__init__()

    def run(self):
        self.obj = walter()
        self.obj.wishuser()
        self.task()

    def task(self):
        # running the while loop infinite times
        while True:
            self.query = takecomand()
            # if user chats (conversation)
            chatresponse = self.obj.chatwalter(self.query)

            # if not in chatbot
            # greet and perform task simultaneously - (can run multiple command at once)
            # eg- hello walter, what is the temperature?
            if chatresponse == 0:
                self.query = self.obj.efficient(self.query)

            if (WindowAutomate(self.query)!= 0):
                print("Done !")

            elif 'open' in self.query or 'launch' in self.query:
                self.obj.open(self.query)
                
            elif 'close' in self.query or 'terminate' in self.query:
                self.obj.close(self.query)
            
            elif 'the date' in self.query:
                speak("Today is " + self.obj.day() + ', ' + self.obj.date())

            elif 'the time' in self.query:
                # declaring the strTime variable to  get the current time according to mearidain
                speak("Sir, The current time is " + self.obj.time())
                
            elif 'screenshot' in self.query or 'take a screenshot' in self.query:
                cwd = os.getcwd()
                pyautogui.screenshot(cwd + r'\image\Image' + str(self.x)+'.png')
                speak("Screenshot is saved as Image" + str(self.x))
                self.x += 1

            elif 'temperature' in self.query:
                speak(self.obj.temperature(self.query))

            elif "weather" in self.query:
                speak(self.obj.weather(self.query))
                # chat.append("Walter: " + chatmsg2) #prints weather in chatbox

            elif "how to" in self.query:
                speak(self.obj.howto(self.query))

            elif "search" in self.query:
                speak(self.obj.web_search(self.query))
            
            elif "near" in self.query or 'nearby' in self.query:
                speak(self.obj.near(self.query))
                # chat.append("Walter: "+ nearby(self.query))   #adding msg to chatbox

            elif "joke" in self.query or 'jokes' in self.query:
                speak(pyjokes.get_joke())
                self.query = takecomand()
                while 'one more' in self.query or 'another one' in self.query or 'once more' in self.query:
                    speak(pyjokes.get_joke())
                    self.query = takecomand()

            elif 'send mail' in self.query:
                self.obj.send_mail(self.query)
            
            elif 'join meet' in self.query or 'create a meet' in self.query or 'create a new meet' in self.query or 'join my class' in self.query:
                try:
                    self.obj.join_meet(self.query)
                except Exception as e:
                    speak("Sorry sir. I am not able to join meet right now")

            elif "my location" in self.query or "where am i" in self.query or "current location" in self.query:
                try:
                    ci, st, co = self.obj.my_location()
                    speak(
                        f"Sir, your current location is {ci} city which is in {st} state and country {co}")

                except Exception as e:
                    speak("Sorry sir, I coundn't fetch your current location. Please try again")

            elif "where is" in self.query or 'location of' in self.query or 'distance of' in self.query:
                target_loc, distance, place = self.obj.location(self.query)
                # city = target_loc["city"]
                state = target_loc["state"]
                country = target_loc["country"]
                try:
                    res = f"{place} is in {state} state of country {country}. It is {distance} km away from your current location"
                    speak(res)
                except:
                    res = "Sorry sir, I couldn't get the location. Please try again"
                    speak(res)

            #battery status
            elif "battery status" in self.query or "remaining battery" in self.query:
                speak(str(self.obj.battery_status()))
                
            elif "set alarm" in self.query:
                try:
                    self.obj.set_alarm(self.query)
                except Exception as e:
                    speak("Sorry sir, i am not able to set the alarm.")

            elif 'who' in self.query or 'what' in self.query or 'when' in self.query or 'where' in self.query or 'how' in self.query or 'why' in self.query or 'which' in self.query:
                #finding answers from API/web/wikipedia
                if chatresponse == 0 :
                    speak(findAns(self.query))
                    
            elif "search " in self.query:
                try:
                    speak("What should I search?")
                    print("What should I search?")
        
                # Get the search query
                    search = takecomand()
                
                    if search:
                    # Open a new tab in Chrome
                      # Wait for Chrome to open

                    # Press Ctrl+L to focus on the address bar
                        pi.hotkey('ctrl', 'l')
                        time.sleep(0.5)  # Give it a moment to focus

                    # Type the search query
                        pi.typewrite(search)
                        time.sleep(0.5)  # Wait for typing to complete

                    # Press Enter to perform the search
                        pi.press('enter')
                        print(f"Searching for: {search}")
                    else:
                        speak("I didn't catch that. Please try again.")
                        print("I didn't catch that. Please try again.")
        
                except Exception as e:
                    speak("Can't open now, please try again later.")
                    print(f"Can't open now, please try again later. Error: {e}") 
            
            elif 'open commandprompt' in self.query:
                os.system("start cmd")
        
            elif 'close commandprompt' in self.query:
                os.system("taskkill /f /im cmd.exe") 
            elif "shut down the system" in self.query:
                os.system("shutdown /s /t 5")
        
            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")
        
            elif 'lock the system' in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")  
            
            elif "go to sleep"in self.query:
                speak('alright then, I am switching off')
                sys.exit()   
                 
            elif "my ip address" in self.query:
                speak("checking")
                try:
                    ipAdd=requests.get('https://api.ipify.org').text 
                    print(ipAdd)
                    speak("your ip address is")
                    speak(ipAdd)
                except Exception as e:
                    speak("network is weak,please try again some time later") 
            else:
                speak("Sorry, I didn't understand. Please say that again.")
                print("Sorry, I didn't understand. Please say that again.")             
startexecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Walter()
        self.ui.setupUi(self)
        self.ui.run_button.clicked.connect(self.starttask)
        self.ui.Terminate.clicked.connect(self.close)
        
    def showText(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        lable_time = current_time.toString('hh:mm:ss')
        lable_date = current_date.toString(Qt.ISODate)
        self.ui.Date.setText(lable_date)
        self.ui.Time.setText(lable_time)
        self.ui.state_of_assistant.setText(listToString(state))
        for item in chat:
            global chat_prev
            if len(chat) != len(chat_prev):
                self.res = listToString(chat[len(chat) - 1])
                self.ui.Chat_box.append(self.res)
                chat_prev.append(self.res)
        
    def starttask(self):
        self.ui.movie = QtGui.QMovie("image/Walter bg.gif")
        self.ui.bg_lab.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("image/footer(line).gif")
        self.ui.footer_img.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showText)
        timer.start(1000) 
        startexecution.start()
        
    # def showquery()

app = QApplication(sys.argv)
friday = Main()
friday.show()
exit(app.exec_())
