# FaZCFimllFiINbREBMeCl3jopJtZnlxfwaGsL9jZ
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


def get_sol_info(plant_Mars: object, sol: str) -> None:
    """Get weather information for a specific sol

    Print the weather information of a sol on Mars
    :param plant_Mars: a json object
    :param sol: a str
    :precondition: mars must be a json object containing weather information on Mars fetched by NASA API;
                    sol must be a str representing a sol on Mars
    :postcondition: print the weather information of a sol on Mars
    :return: the printed weather information of a sol on Mars
    """

    # for each sol
    s = plant_Mars[sol]
    # get season
    season = s['Season']
    # get average atmospheric temperature
    temperature = s['AT']['av']
    # get horizontal wind speed
    hws = s['HWS']['av']
    # get average atmospheric pressure
    pressure = s['PRE']['av']

    # print weather information of that sol
    return print_sol_info(sol=sol, sol_season=season, sol_temperature=temperature, sol_hws=hws, sol_pressure=pressure)


def print_sol_info(sol: str, sol_season: str, sol_temperature: float, sol_hws: float, sol_pressure: float) -> None:
    """Print sol weather information

    Print the weather information of Mars on specific sol.
    :param sol: a str
    :param sol_season: a str
    :param sol_temperature: a float
    :param sol_hws: a float
    :param sol_pressure: a float
    :precondition: sol must be a str representing a sol on Mars; sol_season must be a str;
                    sol_temperature must be a float in °F; sol_hws must be float in m/s;
                    sol_pressure must be a float in Pa
    :postcondition: print the weather information of Mars on specific sol
    """
    print(f'Sol{sol} on Mars is in {sol_season}, average atmospheric temperature is {sol_temperature} °F, '
          f'average horizontal wind speed is {sol_hws} m/s, average atmospheric pressure is {sol_pressure} Pa')


def main():
    """
    Drive the program
    """
    key = 'FaZCFimllFiINbREBMeCl3jopJtZnlxfwaGsL9jZ'
    count = 0
    print('Sol is an Astronomy term stands for day on Mars')

    while True:
        # fetch Mars weather information from NASA API
        weather_on_Mars = get_mars_info(key)
        # get all the sols this API provided
        sol_list = weather_on_Mars['sol_keys']
        # changed the sol every 5 min
        sol_picked = sol_list[count]
        count += 1
        # print the weather information of that sol
        get_sol_info(weather_on_Mars, sol_picked)

        # fetch the latest sol weather information every 5 min
        time.sleep(300)
        # set the count back to 0 when all the sol's weather information in the sol_list is printed
        if count >= 7:
            count = 0


if __name__ == "__main__":
    main()
