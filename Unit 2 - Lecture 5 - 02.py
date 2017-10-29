# lecture
import random

def rollDie():
    """
    returns a random int between 1 and 6
    """
    return random.choice([1, 2, 3, 4, 5, 6])

def testRoll(n = 10):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    print(result)

# testRoll()

# excercise 1
"""
 - A /*static*/ model does not account for the element of time.
    In this type of model, a simulation will give us a snapshot at
    a single point in time.
 - A /*discrete*/ model does not take into account the function of
    time. The state variables change only at a countable number of
    points in time, abruptly from one state to another.
    """

# excercise 2
import random
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    result = 1
    while (result % 2) != 0:
        result = random.randint(0,99)
    return result

# print(genEven())


# excercise 3
import random
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    return 10

import random
def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    return random.choice([10, 12, 14, 16, 18, 20])

import random
def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    return random.randrange(10, 22, 2)


# excercise 4
# dist1 and dist2 are equivalent,
import random
def dist1():
    return random.random() * 2 - 1

def dist2():
    if random.random() > 0.5:
        return random.random()      # not the same as random above
    else:
        return random.random() - 1