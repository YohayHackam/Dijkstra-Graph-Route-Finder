from coordinate import Coordinate

# The Vertex class represents a vertex with coordinates and provides methods to track visited status,
# target distance, and path.
class Vertex(Coordinate):
    
    def __init__(self,cordinate:tuple,coordinates:list) -> None:        
        super().__init__(*cordinate)
        self.visited = False
        self.target_distance = float('inf')
        self.path =[]  
        self.coordinates:list[Coordinate] = [Coordinate(*cords) for cords in coordinates]
        for coordinate in self.coordinates:
            distance = coordinate.calculate_distance(self.longitude,self.latitude)    
            coordinate.set_distance(distance)    
    
    def set_visited(self) -> None:
        self.visited =True
    
    def is_visited(self) -> bool:
        return self.visited
    
    def get_target_distance(self) -> float:
        return self.target_distance    
    
    def set_target_distance(self,distance) -> None:
        self.target_distance = distance
        
    def get_path(self) -> list:
        return self.path  
        
    def set_path(self,path:list) ->None: 
        self.path = path        
    
    def reset_vertex(self) -> None:
        self.visited = False
        self.target_distance = float('inf')
        self.path =[]   

        
        
    
        

    