from time import perf_counter
import timeit

def fib(n):
    if n <= 2: return n
    return fib(n-2) + fib(n-1)

def fib_iter(n):
    if n <= 2: return n
    a, b = 0, 1
    for i in range(0,n):
        a, b = b, a+b
    return b

def measure_running_time(ric, iter):
    values = [ 10, 20, 30 ]
    for value in values:   
        timer0 = perf_counter()
        ric(value)
        timer1 = perf_counter()
        timer2 = perf_counter()
        iter(value)
        timer3 = perf_counter()
        print(f"[perf_counter]: fib_rec({value}): {timer1-timer0} \t\t fib_iter({value}): {timer3-timer2}")
        timer4 = timeit.repeat(lambda: ric(value), repeat=1, number=1)
        timer5 = timeit.repeat(lambda: iter(value), repeat=1, number=1)
        print(f"[timeit.repeat]: fib_rec({value}): {timer4} \t\t fib_iter({value}): {timer5}\n")

measure_running_time(fib, fib_iter)