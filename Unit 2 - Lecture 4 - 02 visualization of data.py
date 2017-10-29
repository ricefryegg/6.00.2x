import pylab as plt

mySample = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(30):
    mySample.append(i)
    myLinear.append(i*2)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.45**i)

# plt.figure('lin')
# plt.xlabel('sample points')
# plt.ylabel('linear function')
# plt.plot(mySample, myLinear)
# plt.figure('quad')
# plt.plot(mySample, myQuadratic)
# #plt.figure('cube')
# #plt.plot(mySample, myCubic)
# #plt.figure('expo')
# #plt.plot(mySample, myExponential)
# # call the same name, if existed, reopen
# plt.figure('quad')
# plt.ylabel('quadratic function')

# plt.figure('lin')
# plt.title('Linear')
# plt.figure('quad')
# plt.figure('cube')
# plt.figure('expo')

# plt.figure('lin')
# plt.clf()
# plt.ylim(0, 1000)
# plt.plot(mySample, myLinear, label = "Linear")
# plt.legend(loc = 'upper left')
# plt.figure('quad')
# plt.clf()
# plt.ylim(0, 1000)
# plt.plot(mySample, myQuadratic, label = "Quadratic")
# plt.figure('lin')
# plt.title('Linear')
# plt.figure('quad')
# plt.title('Quadratic')


# plt.figure('lin quad')
# plt.clf()
# plt.plot(mySample, myLinear, 'b--', label = "Linear", linewidth = 5.0)
# plt.plot(mySample, myQuadratic, 'ro', label = "quadratic", linewidth = 2.0)
# plt.legend(loc = 'upper left')
# plt.title('Linear vs. Quadratic')


# plt.figure('lin quad')
# plt.clf()
# plt.subplot(211)    # row, column, location
# plt.ylim(0,1000)
# plt.plot(mySample, myLinear, 'b--', label = "Linear", linewidth = 5.0)
# plt.subplot(212)    # row, column, location
# plt.ylim(0,1000)
# plt.plot(mySample, myQuadratic, 'ro', label = "quadratic", linewidth = 2.0)
# plt.legend(loc = 'upper left')
# plt.title('Linear vs. Quadratic')


# plt.figure('lin quad')
# plt.clf()
# plt.plot(mySample, myLinear, 'b--', label = "Linear", linewidth = 5.0)
# plt.plot(mySample, myQuadratic, 'ro', label = "quadratic", linewidth = 2.0)
# plt.yscale('log')   # using log scale in y axis
# plt.legend(loc = 'upper left')
# plt.title('Linear vs. Quadratic')

# monthly is monthly deposits
def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    mRate = rate / 12
    for i in range(terms):
        base += [i]
        savings += [savings[-1] * (1 + mRate) + monthly]
    return base, savings

def displayRetireWMonthlies(monthlies, rate, terms):
    plt.figure('retireMonth')
    plt.clf()
    for monthly in monthlies:
        xvals, yvals= retire(monthly, rate, terms)
        plt.plot(xvals, yvals, label = 'retire:' + str(monthly))
        plt.legend(loc = 'upper left')
    plt.show()

# monthlies = [500, 600, 700 ,800, 900, 1000, 1100]
# rate = 0.05
# terms = 40*12
# displayRetireWMonthlies(monthlies, rate, terms)

# #%%
# import matplotlib.pyplot as plt
# import matplotlib as mpl
# import numpy as np

# x = np.linspace(0, 20, 100)
# plt.plot(x, np.sin(x))
# plt.show() 

#%%
# def displayRetreWRates(month, rates, terms):
#     plt.figure('retireRate')
#     plt.clf()
#     for rate in rates:
#         xvals, yvals = retire(month, rate, terms)
#         plt.plot(xvals, yvals, label = 'retire:' + str(month) + ':' + str(int(rate*100)))
#         plt.legend(loc = 'upper left')
#     plt.show()
# displayRetreWRates(800, [0.03, 0.05, 0.07], 40*12)


def displayRetireWMonthsAndRates(monthlies, rates, terms):
    plt.figure('retireBoth')
    plt.clf()
    plt.xlim(30*12, 40*12)  # just display diferences in last 10 years
    monthLabels = ['r', 'b', 'g', 'k']
    rateLabels = ['-', 'o', '--', '^']
    for i in range(len(monthlies)):
        monthly = monthlies[i]
        monthLabel = monthLabels[i%len(monthLabels)]
        for j in range(len(rates)):
            rate = rates[j]
            rateLabels = rateLabels[j%len(rateLabels)]
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals, monthLabel + rateLabels, label = 'retire:' + str(monthly) + ':' \
                                            + str(int(rate*100)))
            plt.legend(loc = 'upper left')
    plt.show()

displayRetireWMonthsAndRates([500, 700, 900, 1100],
                              [0.03, 0.05, 0.07], 40*12)