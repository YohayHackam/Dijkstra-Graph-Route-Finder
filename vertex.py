from coordinate import Coordinate


# This class represents a vertex with a location and a list of coordinates, allowing for finding
# specific coordinates and checking if all coordinates have been visited.
class Vertex(Coordinate):
    
    def __init__(self,location:str,coordinates:list) -> None:
        longitude, latitude = [float(cord) for cord in location.strip('()').split(',')]
        super().__init__(longitude,latitude)
        self.coordinates:list[Coordinate] = [Coordinate(*cords) for cords in coordinates]
        for coordinate in self.coordinates:
            distance = coordinate.calculate_distance(self.longitude,self.latitude)    
            coordinate.set_distance(distance)    
    
    def find_cordinate(self,cords:list[float,float]) -> Coordinate | None:
        if not self.is_visited() and cords == self.get_cords():
            return self 
        for coordinate in self.coordinates:
            if not coordinate.is_visited() and cords == coordinate.get_cords():
                return coordinate
        return None    
    
    def all_cordinates_visited(self) -> bool :        
        for coordinate in self.coordinates:
            if not coordinate.is_visited():
                return False
        return True
        
        
    
        

    