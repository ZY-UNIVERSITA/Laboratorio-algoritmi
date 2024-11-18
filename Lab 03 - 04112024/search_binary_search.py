import math
import test_utils
import test
import numpy as np

def binary_search(array, elem): 
    fromIndex = 0
    toIndex = len(array) - 1

    while fromIndex <= toIndex:
        m = math.floor((fromIndex + fromIndex)/2)

        if array[m] == elem:
            return m
        elif array[m] < elem:
            fromIndex = m + 1
        else:
            toIndex = m - 1
    return -1

def binary_search_rec(array, elem, fromIndex, toIndex): 
    if fromIndex > toIndex:
        return -1

    m = math.floor((fromIndex + toIndex)/2)

    if array[m] == elem:
        return m
    
    if array[m] < elem:
        fromIndex = m + 1
    else:
        toIndex = m - 1

    return binary_search_rec(array, elem, fromIndex, toIndex)


# test: TODO
if __name__ == "__main__":
    # Binary search iterative test
    binarySearchTest = test.returnTestCase(True)
    test_utils.test(binarySearchTest, binary_search)

    print(f"{'-'*100}")

    # Binary search recursive test
    tuple = [
        [],
        [1, 2, 3],
        [1, 2, 3, 4],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]
    binarySearchTest = [
        ((tuple[0], 0, 0, -1), -1),
        ((tuple[1], 3, 0, len(tuple[1]) - 1), 2),
        ((tuple[2], 0, 0, len(tuple[2]) - 1), -1),
        ((tuple[3], 9, 0, len(tuple[3]) - 1), 9)
    ]
    test_utils.test(binarySearchTest, binary_search_rec)