# FaZCFimllFiINbREBMeCl3jopJtZnlxfwaGsL9jZ
import random
import time
import requests
import json


def get_mars_info(key):
    url = f'https://api.nasa.gov/insight_weather/?api_key={key}&feedtype=json&ver=1.0'
    response = requests.get(url)
    response.raise_for_status()
    mars_info = json.loads(response.text)
    return mars_info


def print_mars_info(mars, sol):
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

    while True:
        sol = random.choice(sol_list)
        mars_weather = get_mars_info(key)

        print_mars_info(mars_weather, sol)
        time.sleep(300)


if __name__ == "__main__":
    main()
