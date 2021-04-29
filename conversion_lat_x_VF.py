import math

def conv1(lat,long):
    pi = 3.14
    R = 6371

    # conversion (lat,long) --> (x,y)
    # carte du monde de peters (à plat)
    x = (R*pi*long*45)/180
    y = R*math.sqrt(2)*math.sin(lat)
    
    return x,y
