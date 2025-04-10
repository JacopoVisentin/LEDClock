import numpy as np
import time
import ntplib
from utils import randomCoord
import random

from clock import Clock

def generateNCoords(n: int, max_n: int, max_m: int) -> np.ndarray:
    total = (max_n + 1) * (max_m + 1)
    if n > total:
        raise ValueError("Requested more coordinates than the grid contains")
    # Generate all (x, y) pairs
    all_coords = np.array([(i, j) for i in range(max_n + 1) for j in range(max_m + 1)])
    np.random.shuffle(all_coords)
    return all_coords[:n]

print(generateNCoords(10,2,2))