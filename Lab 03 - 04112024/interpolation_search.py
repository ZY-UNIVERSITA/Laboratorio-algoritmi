import test_utils
import math

def interpolation_search(array, elem, fromIndex, toIndex):
    x0 = fromIndex
    x1 = toIndex
    y = elem

    if x0 <= x1:
        y0 = array[x0]
        y1 = array[x1]

        if y1 - y0 == 0:
            if y0 == elem:
                return x0
        else:
            x = x0 + math.floor(( (x1 - x0) * (y - y0) / (y1 - y0) ))
            
            if x >= x0 or x <= x1:
                if array[x] == elem:
                    return x
                elif array[x] < elem:
                    x0 = fromIndex + 1
                else:
                    x1 = fromIndex - 1
                
                interpolation_search(array, elem, x0, x1)

    return -1

# test: TODO
if __name__ == "__main__":
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
    test_utils.test(binarySearchTest, interpolation_search)