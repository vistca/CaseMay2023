from WeatherRetriever import WeatherRetriever

if __name__ == '__main__':
    print("test")
    data = WeatherRetriever.get_current_weather(29, 120)
    print(data.get_location_name())
    print(data.get_temp())
    print(data.get_description())


