from cordinate import Cordinate
from vertex import Vertex

class Graph():

    def __init__(self,graph_data:dict) -> None:
        self.vertices = []
        for str_cords, path_list in graph_data.items():
            self.vertices.append(Vertex(str_cords, path_list))

    def find_closest_cordinate(self,longitude: float, latitude: float) -> Cordinate:
        min_dist = float('inf')
        closest_codinate = None
        for vertex in self.vertices:
            # Check if vertex is closest cordinate
            dist = vertex.calculate_distance(longitude, latitude)        
            if dist < min_dist:
                min_dist = dist
                closest_codinate = vertex
            # Check cordinate conected to vertex
            for cordinate in vertex.cordinates:
                dist = cordinate.calculate_distance(longitude, latitude)
                if dist < min_dist:
                    min_dist = dist
                    closest_codinate = cordinate
        return closest_codinate
    
    def update_connected_path(self,current:Cordinate,distance:float):
        next_cordinates=[]
        # Mark lowest cordinate distance from target
        if current.target_distance > distance :
            current.set_target_distance(distance)
        # Mark vertex  curdinates lowest distance from target
        if isinstance(current,Vertex) :
            for cordinate in current.cordinates:
                # Check and update distance & path from target
                if cordinate.target_distance > (cordinate.distance + distance) :
                    cordinate.set_target_distance(cordinate.distance + distance)
                    cordinate.set_path([current.get_cords()] + current.get_path())
                # Add only unvisited to visit next 
                if not cordinate.is_visited():
                    next_cordinates.append(cordinate)
        
        # Check all unvisited vertices if connected to this cordinate
        vertices = list(filter(lambda vertex: not vertex.visited and current!=vertex ,self.vertices))
        for vertex in vertices :
            if(cordinate:=vertex.find_cordinate(current.get_cords())):                
                # Check and update distance & path from target
                if cordinate.target_distance > distance :
                    cordinate.set_target_distance(distance)                
                    cordinate.set_path(current.get_path())
                if vertex.target_distance > (cordinate.distance + distance) :
                    vertex.set_target_distance(cordinate.distance + distance)
                    vertex.set_path([cordinate.get_cords()] + cordinate.get_path())                
                next_cordinates.append(vertex)
        # Mark as visited 
        if isinstance(current,Vertex):            
            if current.all_cordinates_visited():
                current.set_visited()
        else:
            current.set_visited()
        # Check Closest cordinates
        next_cordinates.sort(key= lambda cordinate:cordinate.target_distance)        
        for cord in next_cordinates:
            if not cord.is_visited():
                distance = cord.get_target_distance()                
                self.update_connected_path(cord,distance)
        
    def find_path(self,start: Cordinate, end: Cordinate) -> list:
        distance = 0
        current = end
        while not start.is_visited():
            self.update_connected_path(current,distance)           
        return [start.get_cords()] + start.get_path()
    
    