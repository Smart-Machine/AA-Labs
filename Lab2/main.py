import time
import random
from functools import wraps
from sorting_utils import *
from plotting_utils import plot_graph, print_results


def execution_time(func):
    @wraps(func)
    def execution_time_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"{total_time:.6f} seconds")
        return [result, total_time]
    return execution_time_wrapper

@execution_time
def run(func, arr):
    # print(f"Function {func.__name__} is executing")
    print(f"Array with length: {len(arr)} was sorted in ", end="")
    return func(arr)


if __name__=='__main__':

    ARRAY_LIST = [ 
        [random.randint(0, 10000000000000) 
            for _ in range(n * 10000)] 
        for n in range(1, 11)]

    for array in ARRAY_LIST:
        for i in range(len(array)):
            if i < len(array)-1 and abs(array[i] - array[i+1]) == 1: 
                array[i] = random.randint(0, 10000000000000)

    x, y = [], []
    for array in ARRAY_LIST:
        array_copy = array.copy()

        result, execution_time = run(heap_sort, array_copy)
        x.append(len(array))
        y.append(execution_time)

    plot_graph(x, y, "Heap Sort")

    
