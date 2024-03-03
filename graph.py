from coordinate import Coordinate
from vertex import Vertex

# This Python class represents a graph data structure with methods for finding the closest coordinate,
# implementing Dijkstra's algorithm, finding a path between two vertices, and resetting the graph.
class Graph(): 
    def __init__(self,graph_data:dict) -> None:
        self.vertices = []
        for str_cords, path_list in graph_data.items():
            self.vertices.append(Vertex(str_cords, path_list))

    def find_closest_vertex(self,longitude: float, latitude: float) -> Vertex:
        min_dist = float('inf')
        closest_codinate = None
        for vertex in self.vertices:
            # Check if vertex is closest coordinate
            dist = vertex.calculate_distance(longitude, latitude)
            if dist < min_dist:
                min_dist = dist
                closest_codinate = vertex
        return closest_codinate
    
    def get_vertex(self,coordinate:Coordinate) -> Vertex | None:
        for vertex in self.vertices:
            if vertex == coordinate:
                return vertex
                                    
    def dijkstra(self,current:Vertex,distance:float) -> None :
        neighbors =[]
        # Mark lowest coordinate distance from target
        if current.target_distance > distance :
            current.set_target_distance(distance)
        # Mark vertex  coordinates lowest distance from target
        for coordinate in current.coordinates:
            vertex = self.get_vertex(coordinate)
            # Check and update distance & path from target
            if vertex.target_distance > (coordinate.distance + distance) :
                vertex.set_target_distance(coordinate.distance + distance)
                vertex.set_path([current.get_cords()] + current.get_path())
            if not vertex.is_visited():
                neighbors.append(vertex)
        # Mark as visited 
        current.set_visited()
        # Check Closest coordinates
        neighbors.sort(key= lambda vertex:vertex.target_distance)        
        for neighbor in neighbors:
                if not neighbor.is_visited():
                    distance = neighbor.get_target_distance()                
                    self.dijkstra(neighbor,distance)                                           
    
    def find_path(self,start: Vertex, end: Vertex) -> list:
        distance = 0
        current = end
        while not start.is_visited():
            self.dijkstra(current,distance)           
        return [start.get_cords()] + start.get_path()
    
    def reset_graph(self) -> None:
        for vertex in self.vertices:
            vertex.reset_vertex()
    