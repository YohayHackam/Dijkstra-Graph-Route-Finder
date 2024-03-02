import math


# The `Coordinate` class represents a coordinate with latitude and longitude, providing methods to
# manage visited status, distance, target distance, and path.
class Coordinate():
    def __init__(self,latitude:float,longitude:float) -> None:
        self.longitude = longitude
        self.latitude = latitude
        self.visited = False
        self.distance = float('inf')
        self.target_distance = float('inf')
        self.path =[]   

    def get_cords(self) -> tuple[float,float]:
        return (self.latitude,self.longitude)

    def set_visited(self) -> None:
        self.visited =True
    
    def is_visited(self) -> bool:
        return self.visited

    def get_distance(self) -> float:
        return self.distance

    def set_distance(self,distance:float) -> None:
        self.distance=distance
    
    def get_target_distance(self) -> float:
        return self.target_distance    
    
    def set_target_distance(self,distance) -> None:
        self.target_distance = distance
    
    def calculate_distance(self,latitude:float,longitude:float) -> float:
        return math.sqrt((self.latitude - latitude)**2 + (self.longitude - longitude)**2)        
    
    def get_path(self):
        return self.path  
        
    def set_path(self,path:list): 
        self.path = path
    