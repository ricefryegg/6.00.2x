import random, pylab, numpy

# common configuration of histograms
#set line width
pylab.rcParams['lines.linewidth'] = 4
#set font size for titles 
pylab.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
pylab.rcParams['xtick.labelsize'] = 16
#set size of numbers on y-axis
pylab.rcParams['ytick.labelsize'] = 16
#set size of ticks on x-axis
pylab.rcParams['xtick.major.size'] = 7
#set size of ticks on y-axis
pylab.rcParams['ytick.major.size'] = 7
#set size of markers
pylab.rcParams['lines.markersize'] = 10
#set number of examples shown in legends
pylab.rcParams['legend.numpoints'] = 1

def makeHist(data, title, xlabel, ylabel, bins=20):
    pylab.hist(data, bins=bins)
    pylab.title(title)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)

# get the temperatures
def getHighs():
    inFile = open('temperatures.csv')
    population = []
    for l in inFile:
        try:
            tempC = float(l.split(',')[1])
            population.append(tempC)
        except:
            continue
    return population

def getMeansAndSDs(population, sample, verbose=False):
    popMean = sum(population)/len(population)
    sampleMean = sum(sample)/len(sample)
    # draw histogram
    if verbose:
        makeHist(population,
                    'Daily High 1961-2015, Population\n' +\
                    '(mean = ' + str(round(popMean, 2)) + ')',
                    'Celcius Degrees', 'Number Days')
        pylab.figure()
        makeHist(sample,
                    'Daily High 1961-2015, Sample\n' +\
                    '(mean = ' + str(round(sampleMean, 2)) + ')',
                    'Celcius Degrees', 'Number Days')
        pylab.show()
        print('Population mean =', popMean)
        print('Standard deviation of population =',
                numpy.std(population))
        print('Sample mean =', sampleMean)
        print('Standard dviation of sample =',
                numpy.std(sample))
    return popMean, sampleMean,\
           numpy.std(population), numpy.std(sample)

# control the random number
# random.seed(0)
# population = getHighs()
# sample = random.sample(population, 100)
# getMeansAndSDs(population, sample, True)


# see distribution of Means in sample of certain sizes
# random.seed(0)
# population = getHighs()
# sampleSize = 200
# numSamples = 1000
# maxMeanDiff = 0
# maxSDDiff = 0
# sampleMeans = []
# for i in range(numSamples):
#     sample = random.sample(population, sampleSize)
#     popMean, sampleMean, popSD, sampleSD =\
#         getMeansAndSDs(population, sample, verbose=False)
#     sampleMeans.append(sampleMean)
#     if abs(popMean - sampleMean) > maxMeanDiff:
#         maxMeanDiff = abs(popMean - sampleMean)
#     if abs(popSD - sampleSD) > maxSDDiff:
#         maxSDDiff = abs(popSD - sampleSD)
# print('Mean of sample Means =', 
#       round(sum(sampleMeans)/len(sampleMeans), 3))
# print('Standard deviation of sample means =', 
#       round(numpy.std(sampleMeans), 3))
# print('Maximum difference in means =', 
#       round(maxMeanDiff, 3))
# print('Maximum difference in standard deviations =',
#       round(maxSDDiff, 3))
# makeHist(sampleMeans, 'Means of Samples', 'Mean', 'Frequency')
# pylab.axvline(x = popMean, color = 'y')
# pylab.show()


# draw Error Bar Graphs
def showErrorBars(population, sizes, numTrials):
    xVals = []
    sizeMeans, sizeSDs = [], []
    for sampleSize in sizes:
        xVals.append(sampleSize)
        trailMeans = []
        for t in range(numTrials):
            sample = random.sample(population, sampleSize)
            popMean, sampleMean, popSD, sampleSD =\
                getMeansAndSDs(population, sample, verbose=False)
            trailMeans.append(sampleMean)
        sizeMeans.append(sum(trailMeans)/len(trailMeans))
        sizeSDs.append(numpy.std(trailMeans))
    
    pylab.errorbar(xVals, sizeMeans, yerr=1.96*pylab.array(sizeSDs),
                   fmt = 'o', label = '95% Confidence Interval')
    pylab.title('Mean Temperature ('
                + str(numTrials) + ' trials)')
    pylab.xlabel('Sample Size')
    pylab.ylabel('Mean')
    pylab.axhline(y = popMean, color = 'r', label = 'Population Mean')
    pylab.xlim(0, sizes[-1] + 10)
    pylab.legend()
    pylab.figure()
    pylab.show()

# test
population = getHighs()
showErrorBars(population, (50, 100, 200, 300, 400, 500, 600), 50)