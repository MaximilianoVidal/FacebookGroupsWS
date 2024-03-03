import pyautogui
import bot_functions
import facebook_scraper
import source_code_downloader
import time
import pyscreeze

def flatten_list(nested_list):
    """
    This function takes a list of lists and flattens it into a single list.

    Parameters:
    nested_list (list): The nested list to flatten.

    Returns:
    list: The flattened list.
    """
    return [item for sublist in nested_list for item in sublist]


def bot_running_function(limit, keyword):
    """
    This is a bot running function it controls all the execution.. it control the flow of the bot...
    """

    counter = 0
    source_code_downloader.open_close_inspect_element_window()
    full_data_list = []

    while (True):

        html = source_code_downloader.copy_code_using_inspect_element()
        # print(html)

        data_list = facebook_scraper.extract_data(html)
        full_data_list.append(data_list)

        # move the cursor around the screen where facebook icon was located and wait for sometime...

        print(data_list)

        bot_functions.moveCursor_to_the_corner()

        if counter > limit:
            break

        counter += 1
        bot_functions.press_arrow_keys('down', 70)
        time.sleep(3)

    source_code_downloader.open_close_inspect_element_window()

    final_data_list = flatten_list(full_data_list)

    # saves the data into the excel file...
    # full_data_list
    facebook_scraper.save_data_into_excel_file(final_data_list)

    # extract information according to some keywords...
    facebook_scraper.filter_rows_by_keyword(keyword)


if __name__ == "__main__":
    # this is the main function it control all execution related to the main function...

    limit = int(input("How many times you want to scroll down webpage to scrap data: -> "))
    keyword = input("What keyword you want to search in a text after scraping: -> ")

    print(
        "Please sign in to your Facebook account and go to the Facebook group page. After waiting for 20 seconds, the BOT will begin to collect data")
    # print("start /_")
    time.sleep(20)

    bot_running_function(limit=limit, keyword=keyword)
