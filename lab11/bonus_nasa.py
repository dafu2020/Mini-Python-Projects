import time

import requests
import json
from datetime import date
import urllib.request

from PIL import Image


def get_date_today():
    """Get today's date

    :postcondition: get the date of today
    :return: fetched the date of today in yyyy-mm-dd format as a str
    """
    return date.today()


def get_nasa_apod(key: str, end_date: str) -> list:
    """"""
    url = f'https://api.nasa.gov/planetary/apod?api_key={key}&start_date=2020-01-01&end_date={end_date}'
    response = requests.get(url)
    response.raise_for_status()
    nasa_apod_lists = json.loads(response.text)
    return nasa_apod_lists


def get_picture_information(picture: object) -> None:
    """"""

    picture_name = picture['title']

    picture_date = picture['date']

    picture_explanation = picture['explanation']

    picture_url = picture['url']

    print_picture_info(name_of_picture=picture_name, date_of_picture=picture_date,
                       explanation_of_picture=picture_explanation)

    download_picture(picture_url, picture_name)


def print_picture_info(name_of_picture: str, date_of_picture: str, explanation_of_picture: str) -> None:
    """

    :param name_of_picture:
    :param date_of_picture:
    :param explanation_of_picture:
    """
    print(f'Title: {name_of_picture}\n'
          f'Date: {date_of_picture}\n'
          f'Explanation: {explanation_of_picture}\n')


def download_picture(url, picture_name):
    file_name = picture_name + '.png'
    file_path = 'img_src/' + picture_name + '.png'
    urllib.request.urlretrieve(url, file_path)

    open_picture(file_path)


def open_picture(file_name):
    im = Image.open(file_name)
    im.show()
    time.sleep(10)


def main():
    """
    Drive the program
    """
    key = 'FaZCFimllFiINbREBMeCl3jopJtZnlxfwaGsL9jZ'
    print(f'Welcome to our little program!\n'
          f'Here is the Astronomy Picture of the Day (APOD)!\n'
          f'I will show you a different picture every 5 minutes. Stay tune.\n')
    count = 0
    while True:
        user_date = get_date_today()
        nasa_pictures = get_nasa_apod(key, user_date)
        print(len(nasa_pictures))

        get_picture_information(nasa_pictures[count])
        time.sleep(10)
        count += 1
        if count >= len(nasa_pictures):
            return False


if __name__ == "__main__":
    main()
