
# This class provides functionality for the user interface (communication with the terminal)
from WeatherInformation import WeatherInformation
from MyCords import MyCords


class UserInterface:

    # Requests coordinates from the user
    @staticmethod
    def get_cords() -> MyCords:
        print("You have to choose a location by entering its coordinates.")
        print("Write the decimals after the \".\" sign and not after \",\" \n")
        while True:
            user_lat = input("Please enter the latitude: ")
            user_lng = input("Please enter the longitude: ")
            try:
                lat = float(user_lat)
                lng = float(user_lng)
                if -90 < lat > 90 or -180 < lng > 180:
                    raise ValueError
            except ValueError:
                print("Invalid value for the coordinates")
                print("Please try again \n")
                continue
            return MyCords(lat, lng)

    # Presents weather data to the user in a readable way
    @staticmethod
    def present_weather(weather: WeatherInformation):
        print("\nRight now the weather in " + weather.get_location_name() + " is believed to be " + weather.get_description())
        print("The temperature is " + str(weather.get_temp()) + "°C (feels like " + str(weather.get_temp_feel()) + " °C)")
        print("The wind speed is " + str(weather.get_wind_speed()) + "m/s from a direction of " + str(weather.get_wind_direction()) + "°")
        print("The air humidity is " + str(weather.get_humidity()) + "%")
        print("The cloud cover is " + str(weather.get_cloud_cover()) + "%")
        print("The visibility is " + str(weather.get_visibility()) + " meters")

    # Opening statement
    @staticmethod
    def say_welcome():
        print("Welcome the this weather program that is made by Carl 2023")
        print("You will be able to see weather information for almost any location on the globe")
        print("Hope you will  enjoy the experience ;)\n")

    @staticmethod
    def user_wants_to(question: str) -> bool:
        print("\n" + question)
        while True:
            user_input = input("Enter \"y\" for yes and \"n\" for no: ")
            if user_input == "y":
                return True
            elif user_input == "n":
                return False
            print("invalid response, please try again\n")

