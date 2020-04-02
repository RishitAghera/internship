class SpaceAge:
    earth_year = 31557600

    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        return float("%8.2f" % (self.seconds/self.earth_year))

    def on_mercury(self):
        return float("%8.2f" % (self.seconds/(self.earth_year*0.2408467)))

    def on_venus(self):
        return float("%8.2f" % (self.seconds/(self.earth_year*0.61519726)))

    def on_mars(self):
        return float("%8.2f" % (self.seconds/(self.earth_year*1.8808158)))

    def on_jupiter(self):
        return float("%8.2f" % (self.seconds / (self.earth_year * 11.862615)))

    def on_saturn(self):
        return float("%8.2f" % (self.seconds / (self.earth_year * 29.447498)))

    def on_uranus(self):
        return float("%8.2f" % (self.seconds / (self.earth_year * 84.016846)))

    def on_neptune(self):
        return float("%8.2f" % (self.seconds/(self.earth_year*164.79132)))


print(SpaceAge(1210123456).on_uranus())