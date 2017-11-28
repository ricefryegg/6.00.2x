def deviant(numlist):
    numAverage = sum(numlist) / len(numlist)
    total = 0
    for num in numlist:
        total += (num-numAverage)**2
    return total

numlist = [1, 5, 5, 5, 9]
print(deviant(numlist))
print(1.96*5)