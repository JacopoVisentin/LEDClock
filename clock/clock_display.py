import numpy as np

import clock.utils as utils
from clock.clock_timer import ClockTimer


class ClockDisplay:

    def __init__(self):

        self.timer = ClockTimer()
        now = self.timer.now()
        self.hour = now.hour
        self.minute = now.minute

        self.hour_first_digit = 0
        self.hour_second_digit = 0
        self.minute_first_digit = 0
        self.minute_second_digit = 0

        self.hour_first_leds = np.zeros(3)
        self.hour_second_leds = np.zeros((3,3))
        self.minute_first_leds = np.zeros((2,3))
        self.minute_second_leds = np.zeros((3,3))

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
        pass
    def setHourSecondDigit(self, hour: int) -> None:
        hour_str = str(hour)
        if (len(hour_str)) < 2:
            self.hour_second_digit = int(hour)
        if (len(hour_str) == 2):
            self.hour_second_digit = int(hour_str[1])
        pass
    def setMinuteFirstDigit(self, minute: int) -> None:
        minute_str = str(minute)
        if (len(minute_str)) < 2:
            self.minute_first_digit = 0
        if (len(minute_str) == 2):
            self.minute_first_digit = int(minute_str[0])
        pass
    def setMinuteSecondDigit(self, minute: int) -> None:
        minute_str = str(minute)
        if (len(minute_str)) < 2:
            self.minute_second_digit = int(minute)
        if (len(minute_str) == 2):
            self.minute_second_digit = int(minute_str[1])
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
        self.hour_first_leds = np.zeros(3)
        pass
    def resetHourSecondLeds(self) -> None:
        self.hour_second_leds = np.zeros((3,3))
        pass
    def resetMinuteFirstLeds(self) -> None:
        self.minute_first_leds = np.zeros((2,3))
        pass
    def resetMinuteSecondLeds(self) -> None:
        self.minute_second_leds = np.zeros((3,3))
        pass


    def refreshLEDs(self) -> None:
        now = self.timer.now()
        self.hour = now.hour
        self.minute = now.minute
        self.setAllDigits()
        self.setAllLedsOn()


    def __str__(self):
        print("\n")
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