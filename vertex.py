from cordinate import Cordinate


class Vertex(Cordinate):
    
    def __init__(self,location:str,cordinates:list) -> None:
        longitude, latitude = [float(cord) for cord in location.strip('()').split(',')]
        super().__init__(longitude,latitude)
        self.cordinates:list[Cordinate] = [Cordinate(*cords) for cords in cordinates]
        for cordinate in self.cordinates:
            distance = cordinate.calculate_distance(self.longitude,self.latitude)    
            cordinate.set_distance(distance)    
    
    def find_cordinate(self,cords:list[float,float]) -> Cordinate | None:
        if not self.is_visited() and cords == self.get_cords():
            return self 
        for cordinate in self.cordinates:
            if not cordinate.is_visited() and cords == cordinate.get_cords():
                return cordinate
        return None
