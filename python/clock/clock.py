MINUTES_IN_A_DAY = 60 * 24


class Clock:
    def __init__(self, hour, minute):
        self._time = (hour * 60 + minute) % MINUTES_IN_A_DAY

    def __eq__(self, other):
        return self._time == other._time

    def __repr__(self):
        h, m = divmod(self._time, 60)
        return f'{h:02d}:{m:02d}'

    def __add__(self, minutes):
        return Clock(0, self._time + minutes)

    def __sub__(self, minutes):
        return self + -minutes