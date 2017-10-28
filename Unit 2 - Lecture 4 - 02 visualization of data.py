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


plt.figure('lin quad')
plt.clf()
plt.plot(mySample, myLinear, 'b--', label = "Linear", linewidth = 5.0)
plt.plot(mySample, myQuadratic, 'ro', label = "quadratic", linewidth = 2.0)
plt.yscale('log')   # using log scale in y axis
plt.legend(loc = 'upper left')
plt.title('Linear vs. Quadratic')