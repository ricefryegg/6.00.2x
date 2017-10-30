class Location(object):
    def __init__(self, x, y):
        """
        x, y are floats
        """
        self.x = x
        self.y = y
    def move(self, deltaX, deltaY):
        """
        deltaX, deltaY are floats
        """
        return Location(self.x + deltaX, self.y + deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.x - oy
        return (xDist**2 + yDist**2)**0.5
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

class Field(object):
    def __init__(self):
        self.drunks= {}     # hashable
    def addDrunk(self., drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        else:
            return self.drunks[drunk]
    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        # use move attribute to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)

class Drunk(object):
    def __init__(self, Name):
        self.name = name
    def __str__(self):
        return 'This drunk is named' + self.name

# create two knds of drunks
import random
class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0, 1.0), (0.0, -1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)
# have bias on going south
class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0, 0.9), (0.0, -1.1), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

# simulate a single walk
def walk(f, d, numSteps):
    """
    f a Field, d a Drunk in f, drunk in field moves numSteps times
    return: distance between the final location and the location at
            the start of the walk
    """
    start = f.getLoc(d)
    for i in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))

# simulate multiple walks
def simWalks(numSteps, numTrials, drunkClass):
    """
    Assumes numSteps an int >= 0, numTrials an int > 0,
    drunkClass a subclass of Drunk Simulates numTrials
    walks of numSteps steps each. 
    Return: list of the final distances for each trial
    """
    Homer = drunkClass()
    origin = Location(0, 0)
    distances = []
    for i in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(round(walk(f, Homer, numSteps), 1))
    return distances

