import math

# The class `Coordinate` represents a geographical coordinate with longitude and latitude values, and
# provides methods to calculate and set the distance between coordinates.
class Coordinate():
    def __init__(self,longitude:float,latitude:float) -> None:
        self.longitude = longitude
        self.latitude = latitude
        self.distance = float('inf')

    def get_cords(self) -> tuple[float,float]:
        return (self.longitude,self.latitude)

    def get_distance(self) -> float:
        return self.distance

    def set_distance(self,distance:float) -> None:
        self.distance=distance
        
    def calculate_distance(self,longitude:float,latitude:float) -> float:
        return math.sqrt((self.longitude - longitude)**2 + (self.latitude - latitude)**2)        
    

    