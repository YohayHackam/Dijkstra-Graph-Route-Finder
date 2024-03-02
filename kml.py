from simplekml.base import KmlElement
import simplekml

def generate_kml(path:list[tuple]) -> KmlElement:    
    """
    The function generates a KML file with points representing a given path, labeling the start and end
    points.
    
    :param path: The `path` parameter is a list of tuples representing coordinates. Each tuple contains
    the latitude and longitude values of a point on the path
    :type path: list[tuple]
    :return: The function `generate_kml` returns a KML (Keyhole Markup Language) element that contains
    points representing the coordinates in the input `path` list. The points are labeled as "Start
    Point" for the first coordinate, "End Point" for the last coordinate, and "Coordinate i" for all
    other coordinates in between.
    """
    kml = simplekml.Kml()
    for i,cord in enumerate(path):     
        if (i ==0):
            cord_name = "Start Point"
        elif (i== len(path)-1):
            cord_name = "End Point"
        else:
            cord_name = f"Cordinate {i}" 
        kml.newpoint(name=cord_name, coords=[cord]) 
    return kml.kml()
