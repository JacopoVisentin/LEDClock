import numpy as np
import time
import utils
from icecream import ic

from clock import Clock


def main():

    REFRESH_INTERVAL = 5

    clock = Clock()
    last_refreshed_LEDs = time.time()-(REFRESH_INTERVAL-1)

    while True:

        machine_now_epoch = time.time()

        if machine_now_epoch - last_refreshed_LEDs >= REFRESH_INTERVAL:
            clock.refreshLEDs()
            last_refreshed_LEDs = machine_now_epoch        

            utils.clearTerminal()
            print(clock)
        
        time.sleep(0.5)


if __name__ == "__main__":
    main()