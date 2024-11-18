import sys
import math

sizes = [10,100,1000,2000,5000]
sys.setrecursionlimit(2 * max(sizes))


# SELECTION SORT
def minIndex(a, i):
    n = len(a)
    minId = i
    i += 1
    while i < n:
        if a[i] < a[minId]:
            minId = i
        i += 1
    return minId


def selection_sort(a):
    i = 0
    n = len(a)
    while i < n -1:
        minId = minIndex(a, i)
        minValue = a[minId]
        a[i], a[minId] = a[minId], a[i]
        i += 1


# INSERTION SORT
def insertion_in_order(a, i):
    pos = i
    elem = a[i]
    while pos > 0 and a[i] < a[pos-1]:
        pos -= 1

    for j in range(i, pos, -1):
        a[j] = a[j-1] 
    
    a[pos] = elem

def insertion_sort(a):
    i = 1
    n = len(a)
    while i < n:
        insertion_in_order(a, i)
        i += 1


# BUBBLE SORT
def bubble_sort(a):
    swap = True
    i = 0
    n = len(a)
    while swap and i < n - 1:
        swwap = not(swap)
        j = 0
        while j <= n - 2 -i:
            if a[j] > a[j+1]:
                swap = True
                a[j], a[j+1] = a[j+1], a[j]
            j += 1
        i += 1


# MERGE SORT
def merge(a, ia, na, b, ib, nb, temp):
    # print(f"effettuo il merge di: {a[ia:(ia+na)]} e di {b[ib:(ib+nb)]}")
    i = ia
    j = ib
    k = ia
    while i < (ia + na) and j < (ib + nb):
        # print(f"effettuo il merge tra {a[i]} e {a[j]}: {a[i] <= a[j]}")
        if a[i] <= a[j]:
            # print(f"{a[i]} è <= di {a[j]}: {a[i] <= a[j]}")
            temp[k] = a[i]
            i += 1
        else:
            # print(f"{a[i]} è > di {a[j]}: {a[i] > a[j]}")
            temp[k] = a[j]
            j += 1
        k += 1

    while i < (ia + na):
        temp[k] = a[i]
        k += 1
        i += 1

    while j < (ib + nb):
        temp[k] = b[j]
        k += 1
        j += 1

    return temp

def merge_sort_alg(a, i, n, temp):
    if n <= 1:
        return 0
    
    m = math.floor(n/2)
    left = a
    begin_left = i
    n_left = m
    right = a
    begin_right = i+m
    n_right = n-m

    # print(begin_left, n_left, begin_right, n_right)

    merge_sort_alg(left, begin_left, n_left, temp)
    merge_sort_alg(right, begin_right, n_right, temp)
    merge(left, begin_left, n_left, right, begin_right, n_right, temp)

    for j in range(i, i+n):
        a[j] = temp[j]

def merge_sort(a):
    temp = [ 0 for x in range(len(a))]
    merge_sort_alg(a, 0, len(a), temp)


# QUICK SORT
def partition(array, i, n):
    pivotIndex = i
    i = i+1
    k = i
    while i < (pivotIndex+n):
        # print(f"elem: {array[i]} e pivot: {array[pivotIndex]}")
        if array[i] < array[pivotIndex]:
            array[k], array[i] = array[i], array[k]
            k += 1
        i += 1

    array[k-1], array[pivotIndex] = array[pivotIndex], array[k-1]

    return k-1

def quick_sort_alg(array, i, n):
    if n <= 1:
        return 0
    k = partition(array, i, n)

    quick_sort_alg(array, i, k-i)
    quick_sort_alg(array, k+1, n-1-(k-i))

def quick_sort(array):
    quick_sort_alg(array, 0, len(array))


# TEST
if __name__ == '__main__':
    import test_utils
    tests = [
        (([7, 3, 5, 2, 1, 4, 6],), [1, 2, 3, 4, 5, 6, 7], 'random list'),
        (([1, 2, 3, 4, 5, 6, 7],), [1, 2, 3, 4, 5, 6, 7], 'ordered list'),
        (([7, 6, 5, 4, 3, 2, 1],), [1, 2, 3, 4, 5, 6, 7], 'reverse list'),
        (([1, 2, 1, 2, 1, 2, 3, 4, 4, 3],), [1, 1, 1, 2, 2, 2, 3, 3, 4, 4], 'random list with duplicate'),
        (([],), [], 'empty list'),
        (([1],), [1], 'one element list list'),
    ]

    sorting_algorithms = [selection_sort, insertion_sort, bubble_sort, merge_sort, quick_sort]
    test_utils.test_all(tests, sorting_algorithms)
