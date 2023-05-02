
# A class for representing coordinates
class MyCords:
    _lng = 0
    _lat = 0

    def __init__(self, latitude: float, longitude: float):
        self._lat = latitude
        self._lng = longitude

    def longitude(self) -> float:
        return self._lng

    def latitude(self) -> float:
        return self._lat
