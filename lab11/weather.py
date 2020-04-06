# 61e4396df899cdd189cc3e36013ef256
import requests
import json
from datetime import datetime


def to_local_time(unix: int) -> str:
    """Convert the unix timestamp to localtime

    :param unix: an integer
    :precondition: unix must be an integer represent unix timestamp
    :postcondition: convert the unix timestamp to a date and time format for human to read
    :return: the converted date and time as a string
    """
    return datetime.fromtimestamp(unix)


def get_weather():
    url = 'http://api.openweathermap.org/data/2.5/forecast?id=6173331&APPID=61e4396df899cdd189cc3e36013ef256'
    response = requests.get(url)
    response.raise_for_status()
    vancouver_weather = json.loads(response.text)
    return vancouver_weather


def print_day0(weather):
    """Print the weather information for today.

    :param weather:
    :return:
    """
    w = weather['list']
    c = weather['city']
    # get today's weather
    main_weather = w[0]['weather'][0]['main']
    description = w[0]['weather'][0]['description']
    # get sunrise time and sunset time
    sun_rise = c['sunrise']
    sun_set = c['sunset']

    print(f'Current weather in Vancouver: \n'
          f'{main_weather} - {description}\n'
          f'sunrise at: {to_local_time(sun_rise)}\n'
          f'sunset at: {to_local_time(sun_set)}\n')


def print_day1(weather):
    """Print the weather information for tomorrow.

    :param weather:
    :return:
    """
    w = weather['list']
    main_weather = w[8]['weather'][0]['main']
    description = w[8]['weather'][0]['description']

    print(f'Tomorrow: \n'
          f'{main_weather} - {description}\n')


def print_day2(weather):
    """Print the weather information for the day after tomorrow.

    :param weather:
    :return:
    """
    w = weather['list']
    main_weather = w[16]['weather'][0]['main']
    description = w[16]['weather'][0]['description']

    print(f'Two days from now: \n'
          f'{main_weather} - {description}\n')

def print_day3(weather):
    """Print the weather information for the day after the day after tomorrow.

    :param weather:
    :return:
    """
    w = weather['list']
    main_weather = w[24]['weather'][0]['main']
    description = w[24]['weather'][0]['description']

    print(f'Three days from now: \n'
          f'{main_weather} - {description}\n')


def control(weather):
    while True:
        user_input = int(input('How many days of weather you would like to see? \n'
                               '1. Today\n'
                               '2. Today and tomorrow\n'
                               '3. Today, tomorrow, and two days from now\n'
                               '4. Today, tomorrow, two days from now, three days from now\n'
                               'Enter 1, 2, 3, 4 to proceed\n>'))
        if user_input not in [1, 2, 3, 4]:
            print('You have to enter a number from 1-4!')
            continue
        else:
            if user_input == 1:
                print_day0(weather)
                break
            if user_input == 2:
                print_day0(weather)
                print_day1(weather)
                break
            if user_input == 3:
                print_day0(weather)
                print_day1(weather)
                print_day2(weather)
                break
            if user_input == 4:
                print_day0(weather)
                print_day1(weather)
                print_day2(weather)
                print_day3(weather)
                break


def main():
    user_weather = get_weather()
    control(user_weather)


if __name__ == "__main__":
    main()
