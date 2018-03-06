import random

# Monte Carlo Simulation of Pi
# behavior of a single trail
def throwNeedles(numNeedless):
    inCircle = 0
    for needles in range(1, numNeedless + 1, 1):
        x = random.random()
        y = random.random()
        if (x*x + y*y) <= 1:
            inCircle += 1
    fraction = inCircle / float(numNeedless)
    return 4 * fraction

# get standard deviation
def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return std

# multi needles in multi trails
def getEst(numNeedles, numTrails):
    estimates = []
    for t in range(numTrails):
        piGuess = throwNeedles(numNeedles)
        estimates.append(piGuess)
    sDev = stdDev(estimates)
    curEst = sum(estimates)/len(estimates)
    print('Est. = ' + str(curEst) + ', Std. dev = ' + str(round(sDev, 6))\
            + ',  Needles = ' + str(numNeedles))
    return (curEst, sDev)

# test
def estPi(precision, numTrails):
    numNeedles = 1000
    sDev = precision
    while sDev >= precision/2:
        curEst, sDev = getEst(numNeedles, numTrails)
        numNeedles *= 2
    return curEst

# estPi(0.005, 100)


import pylab, numpy, math
# integral of func[f] from a to b copied
def integrate(f, a, b, step):
    yVals, xVals = [], []
    xVal = a
    while xVal < b:
        xVals.append(xVal)
        yVals.append(f(xVal))
        xVal += step
    pylab.plot(xVals, yVals)
    pylab.title('sin(x)')
    pylab.xlim(a, b)
    xUnders, yUnders, xOvers, yOvers = [], [], [], []
    for i in range(1000):
        xVal = random.uniform(a, b)
        yVal = random.uniform(0, 1)
        if yVal < f(xVal):
            xUnders.append(xVal)
            yUnders.append(yVal)
        else:
            xOvers.append(xVal)
            yOvers.append(yVal)
    pylab.plot(xUnders, yUnders, 'ro')
    pylab.plot(xOvers, yOvers, 'ko')
    pylab.xlim(a, b)
    pylab.show()
    ratio = len(xUnders)/(len(xUnders) + len(xOvers))
    print(ratio)
    print(ratio*b)

def one(x):
    return numpy.sin(x)

# integrate(one, 0, math.pi, 0.0001)


# Exercise 4
import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    same = 0
    for i in range(numTrials):
        bucket = [0, 0, 0, 1, 1, 1]     # 0 for green and 1 for red
        select = []
        for n in range(3):
            select.append(random.choice(bucket))
            bucket.remove(select[-1])
        # print(select)
        if select[0] == select[1] and select[1] == select[2]:
            same += 1
    return same / numTrials

# test
test = noReplacementSimulation(10)
print(test)