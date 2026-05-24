class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
    def on_mercury(self):
        return round(round(self.seconds / 31557600, 2) / 0.2408467, 2)
    def on_venus(self):
        return round(round(self.seconds / 31557600, 3) / 0.61519726, 2)
    def on_earth(self):
        return round(self.seconds / 31557600, 2)
    def on_mars(self):
        return round(round(self.seconds / 31557600, 2) / 1.8808158, 2)
    def on_jupiter(self):
        return round(round(self.seconds / 31557600, 2) / 11.862615, 2)
    def on_saturn(self):
        return round(round(self.seconds / 31557600, 2) / 29.447498, 2)
    def on_uranus(self):
        return round(round(self.seconds / 31557600, 2) / 84.016846, 2)
    def on_neptune(self):
        return round(round(self.seconds / 31557600, 2) / 164.79132, 2)
print(SpaceAge(1000000000).on_earth())
print(SpaceAge(2134835688).on_mercury())
print((SpaceAge(2129871239).on_mars()))