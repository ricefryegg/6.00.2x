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


def greedy(items, maxCost, keyFunction):
    '''Assums items a list, maxCost >= 0,
       keyFunction maps elements of items to numbers'''
    itemsCopy = sorted(items, key=keyFunction, reverse=True)

    result = []
    totalValue, totalCost = 0, 0

    for i in range(len(itemsCopy)):
        if totalCost + itemsCopy[i].getCost() <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()

    return (result, totalValue)


# test
def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of item take =', val)
    for item in taken:
        print(' -', item)


# batch test
def testGreedys(foods, maxUnits):
    print('Greedy by value', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.getValue)

    print("\nGreedy by cost", maxUnits, 'calories')
    testGreedy(foods, maxUnits, lambda x: 1 / Food.getCost(x))

    print('\nGreedy by density', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.density)


# brute force
def maxVal(toConsider, avail):
    '''toConsider: a list of items
       avail: weight available
       return: a tuple of total value of a solution to knapsack problem and the list of chosen item'''
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


# brute force test


def testMaxVal(foods, maxUnits, printItems=True):
    print('Search tree', maxUnits, 'calories')
    val, taken = maxVal(foods, maxUnits)
    print('Total value of item taken =', val)
    if printItems:
        for item in taken:
            print(" -", item)


# lecture 1 test
names = ['wine', 'beer', 'pizza', 'burger',
         'fries', 'cola', 'apple', 'donut', 'cake']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = buildMenu(names, values, calories)
testGreedys(foods, 750)
testGreedys(foods, 1000)

# lecture 2 test
testMaxVal(foods, 750)
