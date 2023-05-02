from WeatherRetriever import WeatherRetriever
from UserInterface import UserInterface
from CustomErrors import *


# Lets the user to see the weather for any location
def user_search_for_weather():
    cords = UserInterface.get_cords()
    try:
        weather_data = WeatherRetriever.get_current_weather(cords.latitude(), cords.longitude())
        UserInterface.present_weather(weather_data)
    except MyAPIError:
        print("We are currently having a problem with our server")
    except MyInfoAccessError:
        print("The requested data is unfortunately not accessible")


# The program runs when this function is called
def program_start():
    UserInterface.say_welcome()
    user_search_for_weather()
    while True:
        users_will = UserInterface.user_wants_to("Do you want to see the weather for yet another location?")
        if not users_will:
            print("\nOkay, hope you will use the program soon again")
            return
        user_search_for_weather()


# The main function that will be called first when the file is run
if __name__ == '__main__':
    program_start()






