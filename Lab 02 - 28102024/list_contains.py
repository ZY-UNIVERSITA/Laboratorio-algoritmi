import numpy as np

RANGE = 10

# LIST_CONTAINS FUNCTION
def list_contains(lst, elem):
    i = 0
    n = len(lst)
    while i < n:
        if lst[i] == elem:
            return True
        i+=1
    return False

# TEST FUNCTION
def random(x):
    list = np.arange(0, x, 1)
    random = np.random.randint(0, RANGE*2)
    randomInList = False
    if random in list:
        randomInList = not(randomInList)
    return (list, random, randomInList)

tests = [ random(x) for x in range(RANGE) ]

# RUN TEST
for test in tests:
    testReturn = list_contains(test[0], test[1])
    print(f"Il valore {test[1]} si trova nella lista: {test[0]}: {testReturn}")
    if (test[2] and testReturn) or (not(test[2]) and not(testReturn)):
        print(f"Tutto ok")
    else:
        print(f"Errore")


