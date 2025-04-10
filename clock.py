import numpy as np
import utils



class Clock:

    #  global shapes for any clock
    hour_first_shape = np.zeros(3)
    hour_second_shape = np.zeros((3, 3))
    minute_first_shape = np.zeros((2, 3))
    minute_second_shape = np.zeros((3, 3))

    def __init__(self):
        self.clock_time = utils.getTime()
        
        self.hour_first = Clock.hour_first_shape
        self.hour_second = Clock.hour_second_shape
        self.minute_first = Clock.minute_first_shape
        self.minute_second = Clock.minute_second_shape
        
        self.setDisplay()


    def setHourFirst(self, hour: str) -> None:
        hour_first = int(hour[0])
        self.hour_first[hour_first] = 1
        pass

    def setHourSecond(self, hour: str) -> None:
        hour_second = int(hour[1])
        self.hour_second[hour_second] = 1
        pass
    
    def setMinuteFirst(self, minute: str) -> None:
        minute_first = int(minute[0])
        print(minute_first)
        self.minute_first[minute_first] = 1
        pass

    def setMinuteSecond(self, minute: str) -> None:
        minute_second = int(minute[1])
        print(minute_second)
        self.minute_second[minute_second] = 1
        pass

    def setDisplay(self):
        hours = str(self.clock_time[0])
        minutes = str(self.clock_time[1])
        self.setHourFirst(hours)
        self.setHourSecond(hours)
        self.setMinuteFirst(minutes)
        self.setMinuteSecond(minutes)
        return self


    def __str__(self):
        
        print(self.hour_first, "\n")
        print(self.hour_second, "\n")
        print(self.minute_first, "\n")
        print(self.minute_second, "\n")
        return ""


    def showHourFirst(hour: int):
        digit = (str(hour))[0]
        return digit
