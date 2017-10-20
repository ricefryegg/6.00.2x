class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):
        return self.getValue() / self.getCost()

    def __str__(self):
        return self.name + ':<' + str(self.value) + ', ' + str(self.calories) + '>'


def buildMenu(names, values, calories):
    '''names, values, calories are lists of same length.
       name - a list of strings
       value & calories - lists of nums
       return: list of Foods'''
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu


# brute force
def maxVal(toConsider, avail):
    '''toConsider: a list of items
       avail: weight available
       return: a tuple of total value of a solution to knapsack problem and the list of chosen item'''
    # number of calls
    global numSlowCalls
    numSlowCalls += 1

    # nothing left or no space left
    if toConsider == [] or avail == 0:
        result = (0, ())
    # next item exceeds the space left
    elif toConsider[0].getCost() > avail:
        result = maxVal(toConsider[1:], avail)
    # not exceeds, compare take or not take
    else:
        # take
        nextItem = toConsider[0]
        withVal, withToTake = maxVal(
            toConsider[1:], avail - nextItem.getCost())
        withVal += nextItem.getValue()
        # not take
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        # compare
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result


# dynamic programming with number
# brute force
def fastmaxVal(toConsider, avail, memo = {}):
    '''toConsider: a list of items
       avail: weight available
       return: a tuple of total value of a solution to knapsack problem and the list of chosen item'''
    # counting
    global numFastCalls
    numFastCalls += 1

    # check dict first
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    # nothing left or no space left
    elif toConsider == [] or avail == 0:
        result = (0, ())
    # next item exceeds the space left
    elif toConsider[0].getCost() > avail:
        result = fastmaxVal(toConsider[1:], avail, memo)
    # not exceeds, compare take or not take
    else:
        # take
        nextItem = toConsider[0]
        withVal, withToTake = fastmaxVal(
            toConsider[1:], avail - nextItem.getCost(), memo)
        withVal += nextItem.getValue()
        # not take
        withoutVal, withoutToTake = fastmaxVal(toConsider[1:], avail, memo)
        # compare
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    # update memo
    memo[(len(toConsider), avail)] = result
    return result


# test with different funcs
def testMaxVal(foods, maxUnits, algorithm, printItems = True):
    print("Menu contains", len(foods), "items")
    print('Search tree', maxUnits, 'calories')
    val, taken = algorithm(foods, maxUnits)
    print('Total value of item taken =', val)
    if printItems:
        for item in taken:
            print(" -", item)


# build large menu
import random
def buildLargeMenu(numItems, maxVal, maxCost):
    items = []
    for i in range(numItems):
        items.append(Food(str(i), random.randint(1, maxVal), random.randint(1, maxCost)))
    return items

# dynamic programming test
# slow version
numSlowCalls = 0
numFastCalls = 0
for numItems in range(35):
    items = buildLargeMenu(numItems, 90, 250)
    testMaxVal(items, 750, maxVal, False)
    testMaxVal(items, 750, fastmaxVal, False)
    print("slow calls =", numSlowCalls, "fast calls =", numFastCalls, "\n")

# # fast version
# for numItems in range(0, 5000, 20):
#     numCalls = 0
#     items = buildLargeMenu(numItems, 90, 250)
#     testMaxVal(items, 750, fastmaxVal, False)
#     print("number of calls =", numCalls)
