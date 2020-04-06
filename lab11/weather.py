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
    # unix -= 60*60*7
    return datetime.fromtimestamp(unix)


def get_weather():
    url = 'http://api.openweathermap.org/data/2.5/forecast?id=6173331&APPID=61e4396df899cdd189cc3e36013ef256'
    response = requests.get(url)
    response.raise_for_status()
    vancouver_weather = json.loads(response.text)

    w = vancouver_weather['list']
    c = vancouver_weather['city']
    # get sunrise time and sunset time
    sun_rise = c['sunrise']
    sun_set = c['sunset']

    # print message
    print('Current weather in Vancouver: ')
    print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
    print(f'sunrise at: {to_local_time(sun_rise)}\n'
          f'sunset at: {to_local_time(sun_set)}')
    print('Tomorrow:')
    print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])


def control():
    user_input = int(input('How many days of weather you would like to see? \n'
                           '1. Today\n'
                           '2. Today and tomorrow\n'
                           '3. Today, tomorrow, and two days from now\n'
                           '4. Today, tomorrow, two days from now, three days from now\n'
                           'Enter 1, 2, 3, 4 to proceed\n>'))

    if user_input not in [1, 2, 3, 4]:
        print('You have to enter a number from 1-4!')

    else:
        if user_input == 1:


def main():
    control()


if __name__ == "__main__":
    main()
