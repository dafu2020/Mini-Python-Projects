import subprocess
import time
import urllib
import requests
import json
from datetime import date


def get_date_today():
    """Get today's date

    :postcondition: get the date of today
    :return: fetched the date of today in yyyy-mm-dd format as a str
    """
    return date.today()


def get_nasa_apod(key: str, end_date: str) -> list:
    """Fetch APOD(Astronomy Picture of the Day)s in a time range from NASA API

    :param key: a str
    :param end_date: a str
    :precondition: key must be a str of valid NASA API;
                    end_date must be a str representing a day, in format yyyy-mm-dd
    :postcondition: fetch the APODs information in a time range and store them in a list
    :return: a list containing information of APODs in a time range
    """
    url = f'https://api.nasa.gov/planetary/apod?api_key={key}&start_date=2020-04-01&end_date={end_date}'
    response = requests.get(url)
    response.raise_for_status()
    nasa_apod_lists = json.loads(response.text)
    return nasa_apod_lists


def get_picture_information(picture: object) -> None:
    """Get information of an APOD picture

    :param picture: a json object
    :precondition: picture must be a json object containing weather information of that picture fetched by NASA API;
    :postcondition: print the information of an APOD picture;
                    display the APOD picture
    """

    picture_name = picture['title']

    picture_date = picture['date']

    picture_explanation = picture['explanation']

    picture_url = picture['url']

    print_picture_info(name_of_picture=picture_name, date_of_picture=picture_date,
                       explanation_of_picture=picture_explanation)

    download_picture(picture_url, picture_name)


def print_picture_info(name_of_picture: str, date_of_picture: str, explanation_of_picture: str) -> None:
    """print the information of an APOD picture

    :param name_of_picture: a str
    :param date_of_picture: a str
    :param explanation_of_picture: a str
    :precondition: name_of_picture must be a str;
                    date_of_picture must be a str in yyyy-mm=dd format;
                    explanation_of_picture must be a str that describe the APOD picture
    :postcondition: print out the title, date, explanation information of a APOD picture
    """
    print(f'Title: {name_of_picture}\n'
          f'Date: {date_of_picture}\n'
          f'Explanation: {explanation_of_picture}\n')


def download_picture(url: str, picture_name: str) -> None:
    """Download the APOD picture

    :param url: a str
    :param picture_name: a str
    :precondition: url must be a str of a url of an APOD picture;
                    picture_name must a str of an APOD title
    :postcondition: downloaded the APOD picture by it's URL, stored as a png file with the APOD title
    """
    file_path = 'img_src/' + picture_name + '.png'
    urllib.request.urlretrieve(url, file_path)

    open_picture(file_path)


def open_picture(picture_file: str) -> None:
    """Open an APOD picture

    :param picture_file: a str
    :precondition: picture_file must be as str of the downloaded APOD png filename ending with .png
    :postcondition: open the APOD picture, display it for 30 secs, close that APOD picture
    """
    openImg = subprocess.Popen(["open", picture_file])
    time.sleep(30)
    openImg.kill()


def main():
    """
    Drive the program
    """
    key = 'FqcPKm1Dy8vpZuzvyqnjnEJZk0QsnEa7HnBHuCVg'
    print(f'Welcome to our little program!\n'
          f'Here is the Astronomy Picture of the Day (APOD)!\n'
          f'I will show you a different APOD from the beginning of April to today in every 5 minutes. Stay tune.\n')
    count = 0
    while True:
        user_date = get_date_today()
        nasa_pictures = get_nasa_apod(key, user_date)
        # print(len(nasa_pictures))

        get_picture_information(nasa_pictures[count])
        time.sleep(300)
        count += 1
        if count > len(nasa_pictures):
            return False


if __name__ == "__main__":
    main()
