from coordinate import Coordinate
from vertex import Vertex

# This class represents a graph data structure with methods to find the closest coordinate, update
# connected paths, and find a path between two coordinates.
class Graph():

    def __init__(self,graph_data:dict) -> None:
        self.vertices = []
        for str_cords, path_list in graph_data.items():
            self.vertices.append(Vertex(str_cords, path_list))

    def find_closest_cordinate(self,longitude: float, latitude: float) -> Coordinate:
        min_dist = float('inf')
        closest_codinate = None
        for vertex in self.vertices:
            # Check if vertex is closest coordinate
            dist = vertex.calculate_distance(longitude, latitude)        
            if dist < min_dist:
                min_dist = dist
                closest_codinate = vertex
            # Check coordinate conected to vertex
            for coordinate in vertex.coordinates:
                dist = coordinate.calculate_distance(longitude, latitude)
                if dist < min_dist:
                    min_dist = dist
                    closest_codinate = coordinate
        return closest_codinate
    
    def update_connected_path(self,current:Coordinate,distance:float):
        next_cordinates=[]
        # Mark lowest coordinate distance from target
        if current.target_distance > distance :
            current.set_target_distance(distance)
        # Mark vertex  curdinates lowest distance from target
        if isinstance(current,Vertex) :
            for coordinate in current.coordinates:
                # Check and update distance & path from target
                if coordinate.target_distance > (coordinate.distance + distance) :
                    coordinate.set_target_distance(coordinate.distance + distance)
                    coordinate.set_path([current.get_cords()] + current.get_path())
                # Add only unvisited to visit next 
                if not coordinate.is_visited():
                    next_cordinates.append(coordinate)
        
        # Check all unvisited vertices if connected to this coordinate
        vertices = list(filter(lambda vertex: not vertex.visited and current!=vertex ,self.vertices))
        for vertex in vertices :
            if(coordinate:=vertex.find_cordinate(current.get_cords())):                
                # Check and update distance & path from target
                if coordinate.target_distance > distance :
                    coordinate.set_target_distance(distance)                
                    coordinate.set_path(current.get_path())
                if vertex.target_distance > (coordinate.distance + distance) :
                    vertex.set_target_distance(coordinate.distance + distance)
                    vertex.set_path([coordinate.get_cords()] + coordinate.get_path())                
                next_cordinates.append(vertex)
        # Mark as visited 
        if isinstance(current,Vertex):            
            if current.all_cordinates_visited():
                current.set_visited()
        else:
            current.set_visited()
        # Check Closest coordinates
        next_cordinates.sort(key= lambda coordinate:coordinate.target_distance)        
        for cord in next_cordinates:
            if not cord.is_visited():
                distance = cord.get_target_distance()                
                self.update_connected_path(cord,distance)
        
    def find_path(self,start: Coordinate, end: Coordinate) -> list:
        distance = 0
        current = end
        while not start.is_visited():
            self.update_connected_path(current,distance)           
        return [start.get_cords()] + start.get_path()
    
    