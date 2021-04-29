import math

def conv2(x,y):
    pi = 3.14
    R = 6371
    # conversion (lat,long) --> (x,y)
    # carte du monde de peters (à plat)
    long = (x*180)/(R*pi*45)
    calcul = y/(R*math.sqrt(2))
    lat = math.asin(calcul)
    
    return long,lat