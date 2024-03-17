import re
from bs4 import BeautifulSoup
import pyautogui
import time
import pandas as pd



# keywords and place to look at

KEYWORD = "palabra clave"
LOCATION = "Resistencia"

time.sleep(3)

print(pyautogui.size())  # print the resolution of the screen
print(pyautogui.position())  # print the current position of the mouse


#  switch to a window of facebook opened
def switch_to_facebook():
    pyautogui.hotkey('alt', 'tab')
    time.sleep(2)


# move to search button
def search_keyword():
    pyautogui.moveTo(192, 120, 3)
    pyautogui.leftClick()
    time.sleep(2)
    pyautogui.write(KEYWORD)
    pyautogui.hotkey('enter')
    time.sleep(2)


# send the keyword

def filter_publications():
    pyautogui.moveTo(121, 327, 2)
    pyautogui.doubleClick()
    time.sleep(2)
    pyautogui.moveTo(333, 365, 2)
    pyautogui.click()


# filter by latest ones and zone radio
def filter_location():
    pyautogui.moveTo(176, 575, 2)
    pyautogui.click()
    pyautogui.write(LOCATION)
    time.sleep(1)
    pyautogui.moveTo(193, 636)
    pyautogui.click()
    time.sleep(3)


def main():
    time.sleep(3)
    switch_to_facebook()
    search_keyword()
    filter_publications()
    filter_location()





if __name__ == "__main__":
    main()
