from bs4 import BeautifulSoup
import pandas as pd
import re


# import pandas as pd

def filter_rows_by_keyword(keyword):
    """
    This function reads an Excel file, searches for a specific keyword in a specified column,
    and saves the rows containing that keyword to a new Excel file named "keyword_search.xlsx".

    Parameters:
    file_name (str): The name of the Excel file to read.
    column_name (str): The name of the column to search for the keyword.
    keyword (str): The keyword to search for.

    Returns:
    None
    """
    file_name = 'data.xlsx'
    column_name = 'Data'

    # Read the excel file through pandas as a dataframe
    df = pd.read_excel(file_name)

    # Read the specified column and find the rows containing the keyword
    filtered_rows = df[df[column_name].str.contains(keyword, na=False)]

    # Save the filtered rows to a new Excel file
    # filtered_rows.drop_duplicates()

    filtered_rows.to_excel(f'{keyword}_search.xlsx', index=False)


# Usage:
# filter_rows_by_keyword('your_file.xlsx', 'text', 'your_keyword')


def clean_text(text):
    # List of words to remove
    remove_words = ['See more', 'See original', 'Rate this translation']

    # Remove specific words
    for word in remove_words:
        text = text.replace(word, '')

    # Remove special characters
    text = re.sub(r'\xa0|\t|\n', '', text)

    return text


def save_data_into_excel_file(data_list):
    """
    This function is used to save the data into the Excel document...
    the list will be the final data list... also
    """

    df = pd.DataFrame(data_list, columns=['Data'])
    df.dropna(how='all')
    df.to_excel('data.xlsx', index=False)


def extract_data(html):
    data = []
    soup = BeautifulSoup(html, 'html.parser')

    for tag, attrs in [('div', {'data-ad-comet-preview': 'message', 'data-ad-preview': 'message'}),
                       ('blockquote',
                        {'class': 'xckqwgs x26u7qi x7g060r x1gslohp x11i5rnm xieb3on x1pi30zi x1swvt13 x1d52u69'}),
                       ('div', {'class': 'x1swvt13 x1pi30zi xexx8yu x18d9i69'}), ('div', {'class': 'x5yr21d xyqdw3p'})]:

        for element in soup.find_all(tag, attrs):
            string = element.text
            cleaned_text = clean_text(string)
            data.append(cleaned_text)  # or any other information you want to extract

    # Save the data into a DataFrame and then to an Excel file

    # print(data)

    # df = pd.DataFrame(data, columns=['Data'])
    # df.dropna(how='all')
    # df.to_excel('data.xlsx', index=False)

    return data


def read_html_from_file(file_path):
    with open(file_path, 'r', encoding='utf8') as file:
        html = file.read()
    return html


def scrape_data(html):
    """
    This function scrapes data from the given HTML source code using BeautifulSoup.

    Parameters:
    html (str): The HTML source code to scrape.

    Returns:
    DataFrame: A DataFrame containing the scraped data.
    """
    soup = BeautifulSoup(html, 'html.parser')
    data_list = []

    # x1iorvi4 x1pi30zi x1l90r2v x1swvt13

    # for div in soup.find_all('blockquote', {'class': 'xckqwgs x26u7qi x7g060r x1gslohp x11i5rnm xieb3on x1pi30zi x1swvt13 x1d52u69'}):

    # for div in soup.find_all('div', {'data-ad-comet-preview': 'message', 'data-ad-preview': 'message'}):
    for div in soup.find_all('blockquote',
                             {'class': 'xckqwgs x26u7qi x7g060r x1gslohp x11i5rnm xieb3on x1pi30zi x1swvt13 x1d52u69'}):

        # for tag, attrs in [('div', {'data-ad-comet-preview': 'message', 'data-ad-preview': 'message'}),
        #    ('blockquote', {'class': 'xckqwgs x26u7qi x7g060r x1gslohp x11i5rnm xieb3on x1pi30zi x1swvt13 x1d52u69'})]:

        span = div.find('span',
                        class_='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u x1yc453h')
        if span:
            text = span.text
        else:
            text = div.text
        data_list.append({'text': text})

    df = pd.DataFrame(data_list)
    df.drop_duplicates()  # remove the duplicate rows from the dataframe...

    df.to_excel('data.xlsx', index=False)

    return data_list


def keyword_searching(df, keyword):
    """
    This function searches for a keyword in the DataFrame and creates a new DataFrame with the matching rows.

    Parameters:
    df (DataFrame): The DataFrame to search.
    keyword (str): The keyword to search for.

    Returns:
    DataFrame: A DataFrame containing the rows that contain the keyword.
    """
    df_keyword = df[df['text'].str.contains(keyword)]
    df_keyword.to_excel('keyword_search_data.xlsx', index=False)

    return df_keyword

# html = """ """

# html = read_html_from_file("source_code.txt")
# # # scrap_and_save_text(html)
# list_ = extract_data(html)
# filter_rows_by_keyword("fiverr")
