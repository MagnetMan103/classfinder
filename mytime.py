class Time(object):
    def __init__(self, hours, minutes, period):
        self.hours = hours
        self.minutes = minutes
        self.period = period

    def __str__(self):
        return f'{self.hours}:{self.minutes}{self.period}'

    def convert_to_minutes(self):
        # Convert the time to minutes since midnight
        total_minutes = self.hours * 60 + self.minutes
        if self.hours == 12:
            total_minutes = self.minutes
        if self.period == 'PM':
            total_minutes += 12 * 60  # Add 12 hours for PM
        return total_minutes

    def isbetween(self, time1, time2):
        # Convert the input times to minutes since midnight
        time1_minutes = time1.convert_to_minutes()
        time2_minutes = time2.convert_to_minutes()

        # Get the current time in minutes
        current_time_minutes = self.convert_to_minutes()

        # Check if the current time is between time1 and time2
        return time1_minutes <= current_time_minutes <= time2_minutes


def stringtoobject(timestring):
    a = timestring.find(':')
    hours = int(timestring[:a])
    minutes = int(timestring[a + 1:a + 3])
    period = timestring[a + 3:]
    return Time(hours, minutes, period)

