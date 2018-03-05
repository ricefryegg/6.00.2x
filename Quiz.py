# problem 3
def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    sSum, sLeft = 0, s
    mList = []
    for i in range(len(L)):
        mList.append(sLeft // L[i])
        sSum += L[i] * (sLeft // L[i])
        sLeft -= L[i] * (sLeft // L[i])
    if sLeft == 0:
        return sum(mList)
    return "no solution"

# test = greedySum([10, 5, 1], 14)
# print(test)


# problem 4
def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    maxSum = 0
    for start in range(len(L)):
        for end in range(len(L)):
            maxSum = max(maxSum, sum(L[start:end+1]))
    return maxSum

# test = max_contig_sum([3, 4, -8, 15, -1, 2])
# print(test)


# proble 7
def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    # IMPLEMENT THIS FUNCTION
    n = 0
    while True:
        if test(n) == True:
            return n
        elif test(-n) == True:
            return -n
        n += 1

#### This test case prints 49 ####
def f(x):
    return (x+15)**0.5 + x**0.5 == 15
print(solveit(f))

#### This test case prints 0 ####
def f(x):
    return x == 0
print(solveit(f))