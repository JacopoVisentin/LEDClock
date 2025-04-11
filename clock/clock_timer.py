import time
import numpy as np
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from clock.utils import getReferenceDateTime


class ClockTimer:
    
    def __init__(self, timezone_str = "Europe/Brussels"):
        self.timezone_str = timezone_str
        self.timezone = ZoneInfo(timezone_str)
        self.resync()
    
    def resync(self):
        ntp_time = getReferenceDateTime(self.timezone_str)
        self.reference_datetime = ntp_time
        self.reference_epoch = ntp_time.timestamp()
        self.local_epoch = time.time()
    
        """
        Calculate current time from reference time and how long ago it was fetched
        """
    def now(self) -> datetime:
        elapsed = time.time() - self.local_epoch
        return self.reference_datetime + timedelta(seconds=elapsed)
    
    def time_array(self):
        now = self.now()
        return np.array([now.hour, now.minute, now.second])