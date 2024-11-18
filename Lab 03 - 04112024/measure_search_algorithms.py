import timeit # for measuring time
import search_linear_search # to be impl
import search_binary_search # to be impl
import matplotlib.pyplot as plt # for plotting

import test

# TODO: measure and plot the time of linear_search and binary_search

randomOrderTest = test.returnTestCase()
orderedTest = test.returnTestCase(ordinato=True)
plottingTest = test.returnTestCase(plot=True)

lenEachTest = [ len(pltTest[0][0]) for pltTest in plottingTest ]
timerPlotting = []

# Linear search
def measure_running_time_linear_search(iter):
    # test timer for random array
    for testTuple in randomOrderTest:
        timer1 = timeit.repeat(lambda: iter(testTuple[0][0], testTuple[0][1]), repeat=1, number=1)
        print(f"[timeit.repeat]: linear_search_iterative_unordered_list: {timer1}")

    # test timer for orderer array
    for testTuple in orderedTest:
        timer1 = timeit.repeat(lambda: iter(testTuple[0][0], testTuple[0][1]), repeat=1, number=1)
        print(f"[timeit.repeat]: linear_search_iterative_ordered_list: {timer1}")
    
    # test timer iterative for plotting using worstcase and bigger array
    array = []
    for testTuple in plottingTest:
        timer1 = timeit.repeat(lambda: iter(testTuple[0][0], testTuple[0][1]), repeat=1, number=1)
        array.append(timer1)
    timerPlotting.append(array)
    
measure_running_time_linear_search(search_linear_search.linear_search)


# Binary search
def measure_running_time_binary_search(iter):
    # test timer for orderer array
    for testTuple in orderedTest:
        timer1 = timeit.repeat(lambda: iter(testTuple[0][0], testTuple[0][1]), repeat=1, number=1)
        print(f"[timeit.repeat]: binary_search_iterative: {timer1}")

    # test time for plotting using worstcase and bigger array
    array = []
    for testTuple in plottingTest:
        timer1 = timeit.repeat(lambda: iter(testTuple[0][0], testTuple[0][1]), repeat=1, number=1)
        array.append(timer1)
    timerPlotting.append(array)

measure_running_time_binary_search(search_binary_search.binary_search)


# PLOTTING
label = ["lin_iter", "bin_iter" ]
fig, axes = plt.subplots() 

for i in range(len(timerPlotting)):
    axes.plot(lenEachTest, timerPlotting[i], label=label[i])

axes.set_ylim(0, 1e-01)
axes.set_xscale("log")
axes.set_xlabel("n")
axes.set_ylabel("T(n)")
axes.set_title("Search function")
axes.legend()

plt.show()