class Time:
    # These are the class Attributes:
    max_hours = 24
    max_minutes = 60
    max_seconds = 60

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        """update the time with the new numbers"""
        self.hours, self.minutes, self.seconds = hours, minutes, seconds

    def get_time(self):
        """returns the time formatted"""
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        """Add one second to the time"""
        self.seconds += 1
        if self.seconds >= Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes >= Time.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours >= Time.max_hours:
                    self.hours = 0
        return self.get_time()


time = Time(9, 30, 60)
print(time.next_second())
