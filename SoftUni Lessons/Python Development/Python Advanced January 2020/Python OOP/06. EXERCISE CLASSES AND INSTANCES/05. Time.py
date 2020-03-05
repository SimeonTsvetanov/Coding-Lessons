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
        """returns the time formated"""
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    # def next_second(self, secs_to_add=1):
    #     secs = self.hours * 3600 + self.minutes * 60 + self.seconds
    #     secs += secs_to_add
    #
    #     self.hours = secs // 3600
    #     self.minutes = (secs % 3600) // 60
    #     self.seconds = secs % 60
    #
    #     return self.get_time()

    def next_second(self):
        """update the time with one second (use the class attributes for validation)
         and return the new time (using the get_time() method).
         If the hour gets greater than 24, set it to 0"""

        if self.seconds + 1 > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > Time.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours == Time.max_hours:
                    self.hours = 0
                else:
                    self.hours += 1
            else:
                self.seconds += 1
        else:
            self.seconds += 1
        return self.get_time()


time = Time(9, 30, 60)
print(time.next_second())
