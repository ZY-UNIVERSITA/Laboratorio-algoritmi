import test_utils
import test
import numpy as np

def linear_search(array, elem): 
    i = 0
    n = len(array)
    while i < n:
        if array[i] == elem:
            return i
        i += 1
    return -1

def linear_search_rec(array, elem, index = 0):
    i = index
    n = len(array)

    if i == n:
        return -1
    else:
        if array[i] == elem:
            return i
        return linear_search_rec(array, elem, i+1)
    

# test: TODO
if __name__ == "__main__":
    # Linear search iterative test
    linearSearchTests = test.returnTestCase()
    test_utils.test(linearSearchTests, linear_search)

    print(f"{'-'*100}")

    # Linear search recursive test
    recursiveSearchTests = test.returnTestCase()
    test_utils.test(recursiveSearchTests, linear_search_rec)

