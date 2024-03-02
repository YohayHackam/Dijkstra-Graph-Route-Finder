from simplekml.base import KmlElement
import simplekml

def generate_kml(path:list[tuple]) -> KmlElement:
    
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
    # kml.save("botanicalgarden.kml")    
