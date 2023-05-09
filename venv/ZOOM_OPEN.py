import pyautogui
import webbrowser
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
driver= webdriver.Chrome('c:\software\chromedriver.exe')


url = "https://zoom.us/signin#/login"
time.sleep(2)
zoom_id = "leeison25@googlemail.com"
zoom_passcode = "1Kingdomway"
#double_click_pos = 328, 252
webbrowser.open(url)
time.sleep(5)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(5)
pyautogui.typewrite(zoom_id)
time.sleep(2)
pyautogui.press('enter')
time.sleep(5)
pyautogui.typewrite(zoom_passcode)
time.sleep(5)
pyautogui.press('enter')
time.sleep(2)
#pyautogui.doubleClick(double_click_pos)