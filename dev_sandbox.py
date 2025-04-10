import numpy as np
import time
import ntplib
import utils
import random

from clock import Clock


myClock = Clock()
time = 5
myClock.setHourFirstDigit(time)
myClock.setHourSecondDigit(time)
