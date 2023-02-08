import time
from functools import wraps
from fibonacci_utils import FibonacciNthTerm 
from plotting_utils import plot_graph, print_results

import sys
sys.setrecursionlimit(50000)


def execution_time(func):
    @wraps(func)
    def execution_time_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"Function executed {total_time:.6f} seconds")
        return [result, total_time]
    return execution_time_wrapper

@execution_time
def run(func, n):
    print(f"Function {func.__name__}({n}) is executing")
    return func(n)


if __name__=='__main__':
    FIRST_SEQUENCE = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45]
    SECOND_SEQUENCE = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

    x, y = [], []
    for n in SECOND_SEQUENCE:
        result, execution_time = run(FibonacciNthTerm.tail_recursive_method, n)
        x.append(n)
        y.append(execution_time)
    print_results(x, y)
    plot_graph(x, y, "Tail Recursive Method")

    
