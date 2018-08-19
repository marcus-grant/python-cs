#!/usr/bin/env python3
# from timeit import timeit
# import algorithms.dynamic_programming.dynamic_fib as df
import algorithms.dynamic_programming.dynamic_fib as df
from . import bench_utils

time_func = bench_utils.time_func
avg_time_func = bench_utils.avg_time_func
human_readable_time_str = bench_utils.human_readable_time_str
Spinner = bench_utils.Spinner

def slow_func(n):
    result = [0] * n
    return list(map(lambda x: x**3, result))

def recursive_fib(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    val =  recursive_fib(n - 1) + recursive_fib(n - 2)
    return val

def run_dynamic_vs_recursive_fib_benchmark(fib_num, runs):
    spinner = Spinner()
    print("Running {} runs of fibonacci({}) (recursive):".format(runs, fib_num))
    spinner.start()
    dynamic_time = avg_time_func(df.fibonacci, runs, fib_num)
    dynamic_time_str = human_readable_time_str(dynamic_time)
    f_fib_num = df.fibonacci(fib_num)
    spinner.stop()
    print("fibonacci({}) = {}".format(fib_num, f_fib_num))
    print("Computed in {} (avg)".format(dynamic_time_str))
    print("")
    print("Running {} runs of fibonacci({}) (recursive):".format(runs, fib_num))
    print('')
    spinner.start()
    recursive_time = avg_time_func(recursive_fib, runs, fib_num)
    f_fib_num = recursive_fib(fib_num)
    spinner.stop()
    print("fibonacci({}) = {}".format(fib_num, f_fib_num))
    recursive_str = human_readable_time_str(recursive_time)
    print("Computed in {} (avg)".format(recursive_str))
    speedup = recursive_time / dynamic_time
    print("Speedup of {:.2f}x".format(speedup))
    print()