def deviant(numlist):
    numAverage = sum(numlist) / len(numlist)
    total = 0
    for num in numlist:
        total += (num-numAverage)**2
    return total

# numlist = [1, 5, 5, 5, 9]
# print(deviant(numlist))
# print(1.96*5)


# excercise 3
def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return float('NaN')

    else:
        sumL, sumExp = 0, 0
        for e in L:
            sumL += len(e)
        average = sumL / len(L)
        for e in L:
            sumExp += (len(e)-average)**2
        return (sumExp / len(L))**0.5


# testlist = ['apples', 'oranges', 'kiwis', 'pineapples']
# print(stdDevOfLengths(testlist))

# excercise 4
def stdDev(L):
    sumExp = 0
    average = sum(L) / len(L)
    for e in L:
        sumExp += (e-average)**2
    return ((sumExp / len(L))**0.5) / average

testlist =  [10, 4, 12, 15, 20, 5]
print(stdDev(testlist))