import random

def rollDie():
    """
    returns a random int between 1 and 6
    """
    return random.choice([1, 2, 3, 4, 5, 6])


# sim 1
# def runSim(goal, numTrials):
#     total = 0
#     for i in range(numTrials):
#         result = ''
#         for j in range(len(goal)):
#             result += str(rollDie())
#         if result == goal:
#             total += 1
#     estProbability = round(total/numTrials, 8)
#     print('Probability =', round(1/(6**len(goal)), 8), 
#                 'Estimate:', estProbability)

# runSim('11111', 1000000)


# sim2
def fracBoxCars(numTests):
    numBoxCars = 0
    for i in range(numTests):
        if rollDie() == 6 and rollDie() == 6:
            numBoxCars += 1
    return numBoxCars / numTests
print('Double 6:', str(fracBoxCars(100000)*100) + '%')