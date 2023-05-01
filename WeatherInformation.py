
# A class for holding information about weather for a specific location
class WeatherInformation:

    # Initialization of the attributes
    _temp = 0
    _temp_feel = 0
    _humidity = 0
    _visibility = 0
    _wind_speed = 0
    _wind_direction = 0
    _rain = 0
    _cloud_cover = 0
    _country_code = ""
    _location_name = ""

    # The constructor which assigns values to all attributes
    def __init__(self, temp: float, temp_feel: float, humidity: int, visibility: int, wind_speed: float,
                 wind_direction: int, rain: float, cloud_cover: int, country_code: str, location_name: str):
        self._temp = temp
        self._temp_feel = temp_feel
        self._humidity = humidity
        self._visibility = visibility
        self._wind_speed = wind_speed
        self._wind_direction = wind_direction
        self._rain = rain
        self._cloud_cover = cloud_cover
        self._country_code = country_code
        self._location_name = location_name

    # The attributes should only be accessed by its respective getter method
    def get_temp(self): return self._temp
    def get_temp_feel(self): return self._temp_feel
    def get_humidity(self): return self._humidity
    def get_visibility(self): return self._visibility
    def get_wind_speed(self): return self._wind_speed
    def get_wind_direction(self): return self._wind_direction
    def get_rain(self): return self._rain
    def get_cloud_cover(self): return self._cloud_cover
    def get_country_code(self): return self._country_code
    def get_location_name(self): return self._location_name

