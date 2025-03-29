import random
import numpy as np
from datetime import datetime
from zoneinfo import ZoneInfo
import ntplib



def getDateTime() -> datetime:
    client = ntplib.NTPClient()
    response = client.request('pool.ntp.org')
    timestamp = response.tx_time # convert to epoch time
    current_timezone = "Europe/Brussels" # set timezone explicitly
    brussels_time = datetime.fromtimestamp(timestamp, tz=ZoneInfo(current_timezone)) # convert to human readable time + timezone offset
    return brussels_time

def getTime() -> np.array:
    time = getDateTime().time
    hours = datetime.hour
    minutes = datetime.minute
    seconds = datetime.second
    return np.array([hours, minutes, seconds])

def getDate() -> np.array:
    date = getDateTime().date()
    year = date.year
    month = date.month
    day = date.day
    return np.array([day, month, year])



def randomCoord(max_x: int = 0, max_y: int = 0):
    """returns random 2D coordinate inside given bounds"""
    x = random.randrange(0, max_x, 1)
    y = random.randrange(0, max_y, 1)
    return np.array([x, y])
