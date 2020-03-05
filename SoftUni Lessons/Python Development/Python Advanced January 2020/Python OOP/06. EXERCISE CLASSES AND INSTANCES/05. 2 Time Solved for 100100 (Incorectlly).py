# Takvor's solution of the 5th task:


class Time:
    max_hours = 24
    max_minutes = 60
    max_seconds = 60

    def __init__(self, hours, minutes, seconds):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.time_normalize(hours, minutes, seconds)

    def time_normalize(self, hours, minutes, seconds, add=0):
        if seconds == Time.max_seconds:  # Ox, Judge!
            seconds = 59  # Ay,
        if minutes == Time.max_minutes:  # Ay,
            minutes = 59  # Ay,
        if hours == Time.max_hours:  # Ay,
            hours = 23  # Ay...
        in_seconds = hours * Time.max_minutes * Time.max_seconds + minutes * Time.max_seconds + seconds + add
        in_seconds %= Time.max_hours * Time.max_minutes * Time.max_seconds
        self.hours = in_seconds // (Time.max_minutes * Time.max_seconds)
        in_seconds %= Time.max_minutes * Time.max_seconds
        self.minutes = in_seconds // Time.max_seconds
        in_seconds %= Time.max_seconds
        self.seconds = in_seconds

    def set_time(self, hours, minutes, seconds):
        self.time_normalize(hours, minutes, seconds)

    def get_time(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def next_second(self):
        self.time_normalize(self.hours, self.minutes, self.seconds, 1)
        return self.get_time()
