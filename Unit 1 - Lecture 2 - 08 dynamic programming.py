# slow fib
# in the recursion calculate same fib(n) for numerous time
def fib_slow(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib_slow(n-2) + fib_slow(n-1)

# fast fib
# dynamic programming, trade time for space using dict
def fib_fast(n, fib_save = {}):
    if n == 0 or n == 1:
        return 1
    elif n in fib_save.keys():
        return fib_save[n]
    else:
        fib_save[n] = fib_fast(n-2, fib_save) + fib_fast(n-1, fib_save)
        return fib_save[n]


# test fib
for i in range(121):
    print(i, fib_fast(i))