import numpy as np
import utils
from icecream import ic


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

        self.hour_first_leds = Clock.hour_first_shape
        self.hour_second_leds = Clock.hour_second_shape
        self.minute_first_leds = Clock.minute_first_shape
        self.minute_second_leds = Clock.minute_second_shape

        self.setAllDigits()
        self.setAllLedsOn()


    # Refresh and set all digits from the time
    def setAllDigits(self) -> None:
        self.setHourFirstDigit(self.hour)
        self.setHourSecondDigit(self.hour)
        self.setMinuteFirstDigit(self.minute)
        self.setMinuteSecondDigit(self.minute)
    def setHourFirstDigit(self, hour: int) -> None:
        hour_str = str(hour)
        if (len(hour_str)) < 2:
            self.hour_first_digit = 0
        if (len(hour_str) == 2):
            self.hour_first_digit = int(hour_str[0])
        # ic(self.hour_first_digit)
        pass
    def setHourSecondDigit(self, hour: int) -> None:
        hour_str = str(hour)
        if (len(hour_str)) < 2:
            self.hour_second_digit = int(hour)
        if (len(hour_str) == 2):
            self.hour_second_digit = int(hour_str[1])
        # ic(self.hour_second_digit)
        pass
    def setMinuteFirstDigit(self, minute: int) -> None:
        minute_str = str(minute)
        if (len(minute_str)) < 2:
            self.minute_first_digit = 0
        if (len(minute_str) == 2):
            self.minute_first_digit = int(minute_str[0])
        # ic(self.minute_first_digit)
        pass
    def setMinuteSecondDigit(self, minute: int) -> None:
        minute_str = str(minute)
        if (len(minute_str)) < 2:
            self.minute_second_digit = int(minute)
        if (len(minute_str) == 2):
            self.minute_second_digit = int(minute_str[1])
        # ic(self.minute_second_digit)
        pass
 

    # Set 1s on the led matrix
    def setAllLedsOn(self) -> None:
        self.setHourFirstLedsOn()
        self.setHourSecondLedsOn()
        self.setMinuteFirstLedsOn()
        self.setMinuteSecondLedsOn()
        pass
    def setHourFirstLedsOn(self) -> None:
        self.resetHourFirstLeds()
        led_on_coords = utils.generateNCoords(self.hour_first_digit, 0, 2)
        for coord in led_on_coords:
            self.hour_first_leds[coord[1]] = 1
        pass
    def setHourSecondLedsOn(self) -> None:
        self.resetHourSecondLeds()
        led_on_coords = utils.generateNCoords(self.hour_second_digit, 2, 2)
        for coord in led_on_coords:
            self.hour_second_leds[coord[0], coord[1]] = 1
        pass
    def setMinuteFirstLedsOn(self) -> None:
        self.resetMinuteFirstLeds()
        led_on_coords = utils.generateNCoords(self.minute_first_digit, 1, 2)
        for coord in led_on_coords:
            self.minute_first_leds[coord[0], coord[1]] = 1
        pass
    def setMinuteSecondLedsOn(self) -> None:
        self.resetMinuteSecondLeds()
        led_on_coords = utils.generateNCoords(self.minute_second_digit, 2, 2)
        for coord in led_on_coords:
            self.minute_second_leds[coord[0], coord[1]] = 1
        pass


    # Reset the led matrix to 0 before setting again
    def resetHourFirstLeds(self) -> None:
        self.hour_first_leds = Clock.hour_first_shape
        pass
    def resetHourSecondLeds(self) -> None:
        self.hour_second_leds = Clock.hour_second_shape
        pass
    def resetMinuteFirstLeds(self) -> None:
        self.minute_first_leds = Clock.minute_first_shape
        pass
    def resetMinuteSecondLeds(self) -> None:
        self.minute_second_leds = Clock.minute_second_shape
        pass



    # def __str__(self):
        
    #     print(self.hour_first_leds, "\n\n")
    #     print(self.hour_second_leds, "\n\n")
    #     print(self.minute_first_leds, "\n\n")
    #     print(self.minute_second_leds, "\n\n")
    #     return ""

    def __str__(self):
        emoji_off = "⬛"

        emoji_h_f = "🟥"
        row = self.hour_first_leds
        print(" ".join(emoji_h_f if val == 1 else emoji_off for val in row))
        
        print("\n")

        emoji_h_s = "🟩"
        for row in self.hour_second_leds:
            print(" ".join(emoji_h_s if val == 1 else emoji_off for val in row))

        print("\n")

        emoji_m_f = "🟦"
        for row in self.minute_first_leds:
            print(" ".join(emoji_m_f if val == 1 else emoji_off for val in row))
        
        print("\n")

        emoji_m_s = "🟨"
        for row in self.minute_second_leds:
            print(" ".join(emoji_m_s if val == 1 else emoji_off for val in row))
        
        print("\n")

        return ""