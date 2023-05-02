import requests
from WeatherInformation import WeatherInformation
from CustomErrors import *


# A class for retrieving weather data with the OpenWeather API
class WeatherRetriever:
    API_KEY = "b098b1d3db42f5d2050beee5ec54b664"

    # A method for creating the API URL
    @staticmethod
    def _get_api_url(latitude: float, longitude: float) -> str:
        return ("https://api.openweathermap.org/data/2.5/weather?lat=" +
                str(latitude) + "&lon=" + str(longitude) + "&appid=" +
                WeatherRetriever.API_KEY + "&units=metric")

    # A method responsible for parsing the data from json format to a more user friendly object
    @staticmethod
    def _json_parser(json) -> WeatherInformation:
        try:
            temp = json["main"]["temp"]
            temp_feel = json["main"]["feels_like"]
            humidity = json["main"]["humidity"]
            visibility = json["visibility"]
            wind_speed = json["wind"]["speed"]
            wind_direction = json["wind"]["deg"]
            cloud_cover = json["clouds"]["all"]
            location_name = json["name"]
            description = json["weather"][0]["description"]
            if location_name == "" or location_name == "Globe":
                location_name = "unnamed location"
            return WeatherInformation(temp, temp_feel, humidity, visibility, wind_speed,
                                      wind_direction, cloud_cover, location_name, description)
        except KeyError:   # This error occurs when the json do not contain the requested key
            raise MyInfoAccessError("Requested data is not accessible")

    # A method responsible for making the API call that retrieves the current weather data
    @staticmethod
    def _api_caller(latitude: float, longitude: float) -> dir:
        response = requests.get(WeatherRetriever._get_api_url(latitude, longitude))
        if response.status_code != 200:
            raise MyAPIError("A problem has occurred when calling the Openweathermaps API and the error code is " + str(
                response.status_code))
        return response.json()

    # The only non private method and is the interface of this class that can be used by other classes
    @staticmethod
    def get_current_weather(latitude: float, longitude: float) -> WeatherInformation:
        json = WeatherRetriever._api_caller(latitude, longitude)
        return WeatherRetriever._json_parser(json)
