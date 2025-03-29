import numpy as np
import time
import ntplib
import utils
import random

from clock import Clock


def numberToCoord(element_number, matrix_n, matrix_m):
    
    if element_number > matrix_n*matrix_m -1:
        return "Error"
    
    n_coord = 0
    m_coord = 0
    while (element_number+1 - matrix_n) > 0:
        pass
    
    m_coord = element_number

    return (n_coord, m_coord)