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
            dist = vertex.calculate_distance(longitude, latitude)        
            if dist < min_dist:
                min_dist = dist
                closest_codinate = vertex
            for cordinate in vertex.cordinates:
                dist = cordinate.calculate_distance(longitude, latitude)
                if dist < min_dist:
                    min_dist = dist
                    closest_codinate = cordinate
        return closest_codinate
    
    def update_connected_path(self,current:Cordinate,distance:float):
        connected_cordinates=[]
        # Mark lowest cordinate distance from target
        if current.target_distance > distance :
            current.set_target_distance(distance)
        # Mark vertex curdinates distance from target
        if isinstance(current,Vertex) :
            for cordinate in current.cordinates:                
                if cordinate.target_distance > (cordinate.distance + distance) :
                    cordinate.set_target_distance(cordinate.distance + distance)
                    cordinate.set_path([current.get_cords()] + current.get_path())
                if not cordinate.is_visited():
                    connected_cordinates.append(cordinate)
        # Mark current codinate as visited 
        current.set_visited()
        # Cheack if has other vertex connected to this point
        vertices = list(filter(lambda vertex: not vertex.visited,self.vertices))
        for vertex in vertices :
            if(cordinate:=vertex.find_cordinate(current.get_cords())):                
                if cordinate.target_distance > distance :
                    cordinate.set_target_distance(distance)                
                    cordinate.set_path(current.get_path())
                if vertex.target_distance > (cordinate.distance + distance) :
                    vertex.set_target_distance(cordinate.distance + distance)
                    vertex.set_path([cordinate.get_cords()] + cordinate.get_path())
                # Mark current vertex as visited 
                if not isinstance(cordinate,Vertex) :
                    cordinate.set_visited()
                connected_cordinates.append(vertex)
        connected_cordinates.sort(key= lambda cordinate:cordinate.target_distance)        
        for cord in connected_cordinates:
            if not cord.is_visited():
                distance = cord.get_target_distance()
                self.update_connected_path(cord,distance)
        
    def find_path(self,start: Cordinate, end: Cordinate) -> list:
        # initlise variables 
        distance = 0
        current = end
        while not start.is_visited():
            self.update_connected_path(current,distance)           
        return [start.get_cords()] + start.get_path()
    
    