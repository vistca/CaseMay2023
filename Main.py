from WeatherRetriever import WeatherRetriever
from UserInterface import UserInterface


def program():
    cords = UserInterface.get_cords()
    weather_data = WeatherRetriever.get_current_weather(cords.latitude(), cords.longitude())
    UserInterface.present_weather(weather_data)


if __name__ == '__main__':
    program()


'''
try:

except MyAPIError as e:
    raise e
except MyInfoAccessError as e:
    raise e
'''

