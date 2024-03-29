import pyautogui
import time
from BotGroupsFacebook.botClasses import bot_functions

import pyperclip3


def open_close_inspect_element_window():

    # Press f12 to open the Developer Tools window
    pyautogui.hotkey('f12')
    time.sleep(2)


def copy_website_code():

    """
    This function was specifically copies the code from a website...
    """

    """
    This function is used to click the inspect element of the webpage
    and this function is used to return the signal when code was read...
    """
    try:

        bot_functions.please_wait('D:\ConsultoraPY\ProyectoFaceGroups')
        time.sleep(3)
        # bot_functions.ClickImageOnScreen('./Images/elements.png',1)

    except TypeError:

        # exception appears in case of any additional pop up occur , like Google Translate Tab
        pyautogui.click(2,5)
        time.sleep(1)

    try:

        bot_functions.find_head_tag()
        time.sleep(1)
        png_ = bot_functions.Locate_PNGImageOnScreen('.//Images/body.png')
        pyautogui.click(png_[0]+5, png_[1]+10, button='right')

        time.sleep(1)

        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')

        # one extra down to move keyboard cursor to Copy option
        pyautogui.press('down')

        # time.sleep(1)
        pyautogui.press('left')
        # time.sleep(1)
        pyautogui.press('enter')
        pyautogui.press('enter')

        time.sleep(1)

        source_code = pyperclip3.paste()
        return source_code

    except TypeError:
        return "<html><body>text</body></html>"

    except IndexError:
        return "<html><body>text</body></html>"

    except AttributeError:
        return "<html><body>text</body></html>"


def copy_code_using_inspect_element():

    """
    This function is used to click the inspect element of the webpage
    and this function is used to return the signal when code was read...
    """
    try:

        bot_functions.ClickImageOnScreen('./Screenshots/elements.png', 1)

    except TypeError:

        # exception appears in case of any additional pop up occur , like Google Translate Tab
        pyautogui.click(2,5)
        time.sleep(1)

    try:

        # bot_functions.find_head_tag()
        time.sleep(1)
        png_ = bot_functions.Locate_PNGImageOnScreen('.//Screenshots/body.png')
        pyautogui.click(png_[0]+5, png_[1]+10, button='right')

        time.sleep(1)

        bot_functions.ClickImageOnScreen('./Screenshots/cut.png', 1)

        # pyautogui.press('down')
        # pyautogui.press('down')
        # pyautogui.press('down')
        # pyautogui.press('down')
        # pyautogui.press('down')

        # # one extra down to move keyboard cursor to Copy option
        # pyautogui.press('down')

        # # time.sleep(1)
        # pyautogui.press('left')
        # # time.sleep(1)
        # pyautogui.press('enter')
        # pyautogui.press('enter')

        time.sleep(1)

        source_code = pyperclip3.paste()
        return source_code

    except TypeError:
        return "<html><body>text</body></html>"

    except IndexError:
        return "<html><body>text</body></html>"

    except AttributeError:
        return "<html><body>text</body></html>"



def close_inspect_element():

    # Get the width of the screen

    axes = bot_functions.Locate_PNGImageOnScreen('./Images/settings.png')

    pyautogui.click(axes[0]+70,axes[1]+5)

# print("start...")
# time.sleep(5)
# open_inspect_element_window()
# time.sleep(1)
# c = copy_code_using_inspect_element()
# # close_inspect_element()
# # print(c)

# bot_functions.click_on_inspect_element_scrollbar()
# copy_code_using_inspect_element()

# time.sleep(6)
# copy_code_using_inspect_element()
# copy_source_code_of_website_only()

# data = copy_code_using_inspect_element()
# print(data)