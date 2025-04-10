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

def generateNCoords(n: int, max_n: int, max_m: int) -> np.ndarray:
    
    total_grid_spaces = (max_n + 1) * (max_m + 1)
    if n > total_grid_spaces:
        raise ValueError("Requested more coordinates than the grid contains")
    # Generate all possible coords and shuffle them
    all_coords = np.array([(i, j) for i in range(max_n + 1) for j in range(max_m + 1)])
    np.random.shuffle(all_coords)
    # Return the n first coords
    return all_coords[:n]
