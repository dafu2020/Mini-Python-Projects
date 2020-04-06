# FaZCFimllFiINbREBMeCl3jopJtZnlxfwaGsL9jZ
import random
import time
import requests
import json


def get_mars_info(key: str) -> object:
    """Fetch Mars weather information by using NASA API

    :param key: a str
    :precondition: key must be a str
    :postcondition: fetch Mars weather information and store in a json object
    :return: the fetched Mars weather information as a json object
    """
    url = f'https://api.nasa.gov/insight_weather/?api_key={key}&feedtype=json&ver=1.0'
    response = requests.get(url)
    response.raise_for_status()
    mars_info = json.loads(response.text)
    return mars_info


def print_mars_info(mars: object, sol: str) -> None:
    """Print weather information

    Print the season and average atmospheric temperature of a sol on Mars
    :param mars: a json object
    :param sol: a str
    :precondition: mars must be a json object containing weather information on Mars fetched by NASA API;
                    sol must be a str representing a sol on Mars
    :postcondition: print the season and average atmospheric temperature of a sol on Mars
    """
    s = mars[sol]
    # get season
    season = s['Season']
    # get atmospheric temperature
    temperature = s['AT']['av']

    print(f'Sol{sol} is in {season}, average atmospheric temperature is {temperature} °F')


def main():
    """
    Drive the program
    """
    key = 'FaZCFimllFiINbREBMeCl3jopJtZnlxfwaGsL9jZ'
    # the list  of sol NASA API provided
    sol_list = ['475', '476', '477', '478', '479', '480', '481']

    # fetch the information about the summer and average atmospheric temperature every 5 min
    while True:
        sol = random.choice(sol_list)
        mars_weather = get_mars_info(key)
        print_mars_info(mars_weather, sol)
        # 300 s = 5 min
        time.sleep(300)


if __name__ == "__main__":
    main()
