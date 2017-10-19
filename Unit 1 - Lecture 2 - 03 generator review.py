def gen():
    yield 1
    yield 2

def genFib():
    fib_1 = 0
    fib_2 = 1
    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        fib_next = fib_1 + fib_2
        yield fib_next
        fib_1 = fib_2
        fib_2 = fib_next

fib = genFib()
for n in range(10):
    print(fib.__next__())

for n in genFib():
    print(n, "\n")