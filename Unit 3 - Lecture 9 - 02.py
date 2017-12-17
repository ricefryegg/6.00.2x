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
random.seed(0)
population = getHighs()
sample = random.sample(population, 100)
getMeansAndSDs(population, sample, True)