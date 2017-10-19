# one bag example
# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            # ">>" is one bit right move in binary, equals divde 2**j
            # mod used to present last digit of the binary
            # check jth digit of integer i, if 1 take it
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo


def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    # Your code here
    N = len(items)
    # any given item have 3 condition: bag1, bag2, not taken
    # so enumerate 3**N possible combinations
    for i in range(3**N):
        # fresh start
        bag_1, bag_2 = [], []
        for j in range(N):
            # resembling "Trinary" digits, check jth item from the right, if 1 put in bag_1
            if (i // (3**j)) % 3 == 1:
                bag_1.append(items[j])
            # resembling "Trinary" digits, check jth item from the right, if 2 put in bag_2
            if (i // (3**j)) % 3 == 2:
                bag_2.append(items[j])
        yield (bag_1, bag_2)


a = yieldAllCombos([1, 2, 3, 4, 5, 6, 7, 8, 9])
for n in a:
    print(n)