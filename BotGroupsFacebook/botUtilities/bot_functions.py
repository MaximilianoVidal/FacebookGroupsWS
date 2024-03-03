# ------------------------------------
# libraries required for bot running
# --------------------------------------

import time

import pyautogui
import win32api


# ----------------------------------

def press_tabs_until_appear(image_to_find, image_used_for_find):
    """
    This is a function is used to press tab until system locate image_to_find , we will use image_used_for_find
    """

    please_wait(image_used_for_find)
    time.sleep(1)

    axes = pyautogui.locateOnScreen(image_used_for_find)
    pyautogui.click(axes[0] + 300, axes[1], clicks=1)

    time.sleep(1)

    while (True):

        pyautogui.press('tab')
        # time.sleep(1)

        if LocateImageOnScreen(image_to_find) == True:
            break


def redirect_url(link):
    """
    This function is used to redirect the group link...
    """

    # Press Ctrl + L to selsect the address bar
    pyautogui.hotkey('ctrl', 'l')

    # Wait for the address bar to become active
    time.sleep(2)

    # print("link to write is ",link)

    # Type the URL and press Enter
    pyautogui.typewrite(link, interval=0.05)
    pyautogui.press('enter')
    time.sleep(1)


def ClickImageOnScreen(image_png, total_clicks):
    # this function is used to search the image on screen and returns the co-ordinates

    cordinates = pyautogui.locateCenterOnScreen(image_png, grayscale=True, confidence=0.8)
    pyautogui.click(cordinates[0], cordinates[1], clicks=total_clicks)


def find_image_on_screen(image_png):
    """
    This function is used to find image on screen,
    If it was find return True otherwise False
    """
    if len(Locate_PNGImageOnScreen(image_png)) > 0:
        return True

    else:
        return False


def Locate_PNGImageOnScreen(image_png):
    # this function is used to search the imsage on screen and returns the co-ordinates
    # time.sleep(4)

    if pyautogui.locateOnScreen(image_png, grayscale=True, confidence=0.8) != None:
        cordinates = pyautogui.locateOnScreen(image_png, grayscale=True, confidence=0.8)
        position = []
        position.append(cordinates[0])
        position.append(cordinates[1])
        return position
    else:
        return []


def move_cursor():
    """
    This function is used to move the cursor to left side of screen where Twitter Icon was place
    """

    cordinates = Locate_PNGImageOnScreen('.//Images/ICON.png')
    pyautogui.click(cordinates[0] + 120, cordinates[1])
    time.sleep(1)


def Click_PNGImageOnScreen(image_png, _x, _y, total_clicks):
    # this function is used to search the image on screen and returns the co-ordinates

    if len(Locate_PNGImageOnScreen(image_png)) > 0:

        cordinates = pyautogui.locateOnScreen(image_png, grayscale=True, confidence=0.8)
        pyautogui.click(cordinates[0] + _x, cordinates[1] + _y, clicks=total_clicks)  # (x,y)

    else:
        pass


def LocateImageOnScreen(image_png):
    # this function is used to search the image on screen and returns the co-ordinates
    # time.sleep(4)

    if pyautogui.locateOnScreen(image_png, grayscale=True, confidence=0.8) != None:
        return True
    else:
        return False


def locate_when_appear(png_image):
    """
    This function is used to find image when it appears...
    It prevents the unwanted time sleeps
    """
    counter = 0
    while (True):
        if LocateImageOnScreen(png_image) == True:
            break
        else:
            time.sleep(1)

        counter += 1
        if counter == 7:
            break


def moveCursor_to_the_corner():
    """
    this function is used to move the cursor around the corner..
    """

    axes = Locate_PNGImageOnScreen('./Screenshots/logo.png')
    pyautogui.click(axes[0], axes[1] + 300, clicks=1)


def click_when_appear(png_image):
    """
    This function is used to click on image when it appears...
    It prevents the unwanted time sleeps
    """

    while (True):
        if LocateImageOnScreen(png_image) == True:
            ClickImageOnScreen(png_image, 1)
            break
        else:
            time.sleep(0.5)


def press_arrow_keys(arrow_, times):
    for i in range(0, times):
        pyautogui.hotkey(arrow_)


def press_tab_key(times):
    for i in range(0, times):
        pyautogui.press('tab')


def please_wait(png_image):
    """
    Wait until appear...
    """

    while (True):

        if len(Locate_PNGImageOnScreen(png_image)) > 0:
            break

        time.sleep(1)


def please_wait_for_sometime(png_image):
    """
    Wait until appear...
    """

    flag = True
    counter = 0

    while True:

        if len(Locate_PNGImageOnScreen(png_image)) > 0:
            flag = True
            break

        time.sleep(1)
        counter += 1

    if counter >= 10:
        return False

    else:
        return flag


def click_on_inspect_element_scrollbar():
    axes = Locate_PNGImageOnScreen('./Images/settings.png')

    for i in range(0, 7):
        pyautogui.click(axes[0] + 75, axes[1] + 25)


def find_head_tag():
    axes = Locate_PNGImageOnScreen('./Images/settings.png')

    while (True):

        if find_image_on_screen('./Images/body.png') == True:
            break

        else:
            pyautogui.click(axes[0] + 75, axes[1] + 245)

        time.sleep(1)


def scrolling_down(scrolling_down_counter):
    # this function is used to scroll down the screen...

    for i in range(0, scrolling_down_counter):
        pyautogui.press('down')


def scrolling_function(cordinates, total_clicks):
    """
    This function is used to scroll down the screen
    """

    height = win32api.GetSystemMetrics(1)
    y = height - 82

    pyautogui.click(cordinates[0] + 184, y, clicks=total_clicks)
    # pyautogui.click(cordinates[0]+50,cordinates[1]-13,clicks=total_clicks)


def press_backspace(number):
    for i in range(0, number):
        pyautogui.press("backspace")


def redirect_file_path(filename, folder_path):
    axes = pyautogui.locateOnScreen('.//Images/up.png')
    pyautogui.click(axes[0] + 700, axes[1], clicks=1)

    time.sleep(1)
    pyautogui.press('backspace')
    time.sleep(1)

    pyautogui.typewrite(folder_path, interval=0.05)
    pyautogui.press('enter')
    time.sleep(1)

    # click on filename...
    axes = pyautogui.locateOnScreen('.//Images/filename.png')
    pyautogui.click(axes[0] + 300, axes[1], clicks=1)
    time.sleep(1)

    pyautogui.typewrite(filename, interval=0.05)
    pyautogui.press('enter')

    # auto-check condition to terminate the
    time.sleep(7)

    if find_image_on_screen('.//Images/post.png') == False:
        # print("Post image not found...")

        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        time.sleep(1)

        pyautogui.press('enter')


def maximimize_chrome():
    ClickImageOnScreen('./Images/maximum.png', 1)

# time.sleep(4)
# ClickImageOnScreen('./Images/elements.png',1)

# click_on_inspect_element_scrollbar()
# axes = Locate_PNGImageOnScreen('./Images/all_filters.png')
# scrolling_function(axes,1)
# find_head_tag()
