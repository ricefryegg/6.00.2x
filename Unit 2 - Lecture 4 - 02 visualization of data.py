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

plt.plot(mySample, myLinear)
plt.plot(mySample, myQuadratic)
plt.plot(mySample, myCubic)
plt.plot(mySample, myExponential)