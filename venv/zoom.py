import pyautogui
import webbrowser
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys
import time
driver= webdriver.Chrome('c:\software\chromedriver.exe')

import os
import subprocess
os.remove(r"C:\Users\wanka\AppData\Local\Google\Chrome\User Data\Profile 8\Network\Cookies")

from tkinter import *
from tkinter import ttk
#Create an instance of Tkinter frame
root = Tk()
#Set the geometry of Tkinter frame
root.geometry("1000x200")

def Close():
    root.destroy()

Label(root, text=" Please do not use Mouse and Keyboard while Zoom is Loading....", font=('Helvetica 14')).pack(pady=20)
#Create a button in the main Window to open the popup
ttk.Button(root, text= "Close", command= Close).pack()
root.mainloop()

os.chdir(r"C:\Users\wanka\Documents\OnlyM\Media")
all_files = os.listdir()

for f in all_files:
    os.remove(f)

print(os.listdir())

url = "https://zoom.us/signin#/login"
time.sleep(2)
zoom_id = "leeison25@googlemail.com"
zoom_passcode = "1Kingdomway"
#double_click_pos = 328, 252
webbrowser.open(url)
time.sleep(2)
pyautogui.press(['tab', 'tab', 'tab', 'tab'])# press the TAB key
pyautogui.press('enter') # press the Enter key
time.sleep(5)
webbrowser.open(url)
time.sleep(4)
pyautogui.typewrite(zoom_id)
time.sleep(2)
pyautogui.press('enter')
time.sleep(5)
pyautogui.typewrite(zoom_passcode)
time.sleep(5)
pyautogui.press('enter')
time.sleep(2)


url = "https://zoom.us/join"
zoom_id = "9708820352"
zoom_passcode = "1914"
#double_click_pos = 328, 252
webbrowser.open(url)
time.sleep(10)
pyautogui.typewrite(zoom_id)
time.sleep(2)
pyautogui.press('enter')
time.sleep(5)
pyautogui.typewrite(zoom_passcode)
time.sleep(5)
pyautogui.press('enter')
time.sleep(2)
#pyautogui.doubleClick(double_click_pos)

#command  = (r'"C:\Merthyr_Host.bat"')
#subprocess.Popen(command)
subprocess.call([r'C:\Merthyr_Host.bat'])