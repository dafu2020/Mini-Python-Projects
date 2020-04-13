# 61e4396df899cdd189cc3e36013ef256
import requests
import json
from datetime import datetime


def get_today(key: str, city: str) -> dict:
    """Get current weather info

    :param key: a str
    :param city: a str
    :precondition: key must be a str representing api key;
                    city must be a str representing city id
    :postcondition: fetch current weather information from Openweather api
    :return: the fetched weather information as a dict
    """
    url = f'https://api.openweathermap.org/data/2.5/weather?id={city}&appid={key}'
    response = requests.get(url)
    response.raise_for_status()
    current_weather = json.loads(response.text)
    return current_weather


def get_future(key: str, city: str) -> dict:
    """Get future weather info

    :param key: a str
    :param city: a str
    :precondition: key must be a str representing api key;
                    city must be a str representing city id
    :postcondition: fetch future weather information from Openweather api
    :return: the fetched weather information as a dict
    """
    url = f'http://api.openweathermap.org/data/2.5/forecast?id={city}&APPID={key}'
    response = requests.get(url)
    response.raise_for_status()
    vancouver_weather = json.loads(response.text)
    return vancouver_weather


def print_day0(weather: dict):
    """Print the weather information for today.

    :param weather: a dict
    :precondition: weather must be a dict containing weather information from Openweather API
    :postcondition: print out weather information for today
    """
    c = weather['sys']
    # get today's weather
    time = weather['dt']
    main_weather = weather['weather'][0]['main']
    description = weather['weather'][0]['description']
    # get sunrise time and sunset time
    sun_rise = c['sunrise']
    sun_set = c['sunset']

    print(f'Current weather in Vancouver at: {datetime.fromtimestamp(time)}\n'  # convert unix time to local time
          f'{main_weather} - {description}\n'
          f'sunrise at: {datetime.fromtimestamp(sun_rise)}\n'
          f'sunset at: {datetime.fromtimestamp(sun_set)}\n')


def print_day1(weather: dict) -> None:
    """Print the weather information for tomorrow.

    :param weather: a dict
    :precondition: weather must be a dict containing weather information from Openweather API
    :postcondition: print out weather information for tomorrow
    """
    w = weather['list']
    time = w[5]['dt_txt']
    main_weather = w[5]['weather'][0]['main']
    description = w[5]['weather'][0]['description']

    print(f'Tomorrow at: {time}\n'
          f'{main_weather} - {description}\n')


def print_day2(weather: str) -> None:
    """Print the weather information for the day after tomorrow.

    :param weather: a dict
    :precondition: weather must be a dict containing weather information from Openweather API
    :postcondition: print out weather information for the day after tomorrow
    """
    w = weather['list']
    time = w[13]['dt_txt']
    main_weather = w[13]['weather'][0]['main']
    description = w[13]['weather'][0]['description']

    print(f'Two days from now at: {time}\n'
          f'{main_weather} - {description}\n')


def print_day3(weather: str) -> None:
    """Print the weather information for the day after the day after tomorrow.

    :param weather: a dict
    :precondition: weather must be a dict containing weather information from Openweather API
    :postcondition: print out weather information for the day after the day after tomorrow
    """
    w = weather['list']
    time = w[21]['dt_txt']
    main_weather = w[21]['weather'][0]['main']
    description = w[21]['weather'][0]['description']

    print(f'Three days from now at: {time}\n'
          f'{main_weather} - {description}\n')


def control(current_weather: dict, future_weather: dict) -> None:
    """Control the respond of from the weather API

    :param current_weather: a dict
    :param future_weather: a dict
    :precondition: current_weather must be a dict containing weather information from Openweather API;
                    future_weather must be a dict containing weather information from Openweather API;
    :postcondition: executed user command and print corresponding weather information
    """
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
                print_day0(current_weather)
                break
            if user_input == 2:
                print_day0(current_weather)
                print_day1(future_weather)
                break
            if user_input == 3:
                print_day0(current_weather)
                print_day1(future_weather)
                print_day2(future_weather)
                break
            if user_input == 4:
                print_day0(current_weather)
                print_day1(future_weather)
                print_day2(future_weather)
                print_day3(future_weather)
                break


def main():
    """
    Drive the program
    """
    key = '61e4396df899cdd189cc3e36013ef256'
    city = '6173331'
    # get weather for today and future
    current_weather = get_today(key, city)
    future_weather = get_future(key, city)

    control(current_weather, future_weather)


if __name__ == "__main__":
    main()
