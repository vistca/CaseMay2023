import requests
from WeatherInformation import WeatherInformation
from CustomErrors import *


# A class for retrieving weather data with the OpenWeather API
class WeatherRetriever:
    API_KEY = "b098b1d3db42f5d2050beee5ec54b664"

    # A method for formatting
    @staticmethod
    def _get_api_url(latitude: float, longitude: float) -> str:
        return ("https://api.openweathermap.org/data/2.5/weather?lat=" +
                str(latitude) + "&lon=" + str(longitude) + "&appid=" +
                WeatherRetriever.API_KEY + "&units=metric")

    @staticmethod
    def _json_parser(json) -> WeatherInformation:
        print(json)
        try:
            temp = json["main"]["temp"]
            temp_feel = json["main"]["feels_like"]
            humidity = json["main"]["humidity"]
            visibility = json["visibility"]
            wind_speed = json["wind"]["speed"]
            wind_direction = json["wind"]["deg"]
            rain = json["rain"]["1h"]
            cloud_cover = json["clouds"]
            country_code = json["sys"]["country"]
            location_name = json["name"]
        except KeyError:
            raise MyInfoAccessError("Requested data is not accessible")
        return WeatherInformation(temp, temp_feel, humidity, visibility, wind_speed,
                                  wind_direction, rain, cloud_cover, country_code, location_name)

    @staticmethod
    def api_caller(latitude: float, longitude: float) -> dir:
        response = requests.get(WeatherRetriever._get_api_url(latitude, longitude))
        if response.status_code // 100 != 2:
            raise MyAPIError("A problem has occurred when calling the Openweathermaps API and the error code is " + str(
                response.status_code))
        return response.json()

    @staticmethod
    def get_current_weather(latitude: float, longitude: float) -> WeatherInformation:
        try:
            json = WeatherRetriever.api_caller(latitude, longitude)
            return WeatherRetriever._json_parser(json)
        except MyAPIError as e:
            raise e
        except MyInfoAccessError as e:
            raise e
