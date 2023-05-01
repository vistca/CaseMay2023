from WeatherRetriever import WeatherRetriever

if __name__ == '__main__':
    print("test")
    data = WeatherRetriever.get_current_weather(160, 15)
    print(data.get_location_name())
    print(data.get_wind_direction())




# 57.689, 11.648