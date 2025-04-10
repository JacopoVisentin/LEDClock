import numpy as np
import utils



class Clock:

    #  global shapes for any clock
    hour_first_shape = np.zeros(3)
    hour_second_shape = np.zeros((3, 3))
    minute_first_shape = np.zeros((2, 3))
    minute_second_shape = np.zeros((3, 3))

    def __init__(self):
        # TODO something with this
        # self.clock_time = utils.getTime()
        self.clock_time = np.array([17, 38, 00])
        self.hour = self.clock_time[0]
        self.minute = self.clock_time[1]

        self.hour_first_digit = 0
        self.hour_second_digit = 0
        self.minute_first_digit = 0
        self.minute_second_digit = 0



    def refreshTime(self) -> None:
        self.hour_first_digit = self.setHourFirstDigit(self.hour)
        self.hour_second_digit = self.setHourSecondDigit(self.hour)
        self.minute_first_digit = self.setMinuteFirstDigit(self.minute)
        self.minute_second_digit = self.setMinuteSecondDigit(self.minute)


    def setHourFirstDigit(self, hour: int) -> None:
        hour_str = str(hour)
        if (len(hour_str)) < 2:
            self.hour_first_digit = 0
        if (len(hour_str) == 2):
            self.hour_first_digit = hour_str[0]
        print(self.hour_first_digit)
        pass

    def setHourSecondDigit(self, hour: int) -> None:
        hour_str = str(hour)
        if (len(hour_str)) < 2:
            self.hour_second_digit = hour
        if (len(hour_str) == 2):
            self.hour_second_digit = hour_str[1]
        print(self.hour_second_digit)
        pass
    
    def setMinuteFirstDigit(self, minute: int) -> None:
        minute_str = str(minute)
        if (len(minute_str)) < 2:
            self.minute_first_digit = 0
        if (len(minute_str) == 2):
            self.minute_first_digit = minute_str[0]
        print(self.minute_first_digit)
        pass

    def setMinuteSecondDigit(self, minute: int) -> None:
        minute_str = str(minute)
        if (len(minute_str)) < 2:
            self.minute_second_digit = 0
        if (len(minute_str) == 2):
            self.minute_second_digit = minute_str[0]
        print(self.minute_second_digit)
        pass

    def setDisplay(self):
        # hours = str(self.clock_time[0])
        # minutes = str(self.clock_time[1])
        # self.setHourFirst(hours)
        # self.setHourSecond(hours)
        # self.setMinuteFirst(minutes)
        # self.setMinuteSecond(minutes)
        return self


    def __str__(self):
        
        # print(self.hour_first, "\n")
        # print(self.hour_second, "\n")
        # print(self.minute_first, "\n")
        # print(self.minute_second, "\n")
        return ""

