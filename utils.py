import random
import numpy as np
from datetime import datetime
from zoneinfo import ZoneInfo
import ntplib



#############################
### TIME INFO EXTRACTION
#############################

def getDateTime() -> datetime:
    client = ntplib.NTPClient()
    response = client.request('pool.ntp.org')
    timestamp = response.tx_time # convert to epoch time
    current_timezone = "Europe/Brussels" # set timezone explicitly
    brussels_time = datetime.fromtimestamp(timestamp, tz=ZoneInfo(current_timezone)) # convert to human readable time + timezone offset
    return brussels_time

def getTime() -> np.array:
    time = getDateTime().time()
    hours = time.hour
    minutes = time.minute
    seconds = time.second
    return np.array([hours, minutes, seconds])

def getDate() -> np.array:
    date = getDateTime().date()
    year = date.year
    month = date.month
    day = date.day
    return np.array([day, month, year])




#############################
### COORDINATES
#############################

def randomCoord(max_n: int = 0, max_m: int = 0):
    """returns random 2D coordinate inside given bounds"""
    n = random.randint(0, max_n)
    m = random.randint(0, max_m)
    return np.array([n, m])

def generateNCoords(n: int, max_n: int, max_m: int) -> np.array:
    
    if n > (max_n+1)*(max_m+1):
        raise ValueError("Requested more led coordinates than there exists")
    
    coords = []
    while (len(coords) < n):
        new_coord = randomCoord(max_n, max_m)
        if not any((new_coord == element).all() for element in coords):
            coords.append(new_coord)
        del new_coord
    
    return np.array(coords)
