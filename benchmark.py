#!/usr/bin/env python3
import argparse
import sys
import benchmarks.bench_dyn_fib as df_bench

script_desc = "Benchmark various modules within this one.\n"
parser = argparse.ArgumentParser(description=script_desc)

parser.add_argument('--preset')

def print_valid_preset_names():
    print("dynamic-fib")

def run_preset(p_name):
    if p_name == 'dynamic-fib':
        df_bench.run_dynamic_vs_recursive_fib_benchmark(36, 4)
        df_bench.run_dynamic_vs_recursive_fib_benchmark(32, 16)
        df_bench.run_dynamic_vs_recursive_fib_benchmark(16, 64)
        df_bench.run_dynamic_vs_recursive_fib_benchmark(4, 256)
        return
    print("Invalid preset given!\nPlease use one of these preset names:")
    print_valid_preset_names()
    sys.exit(1)

if __name__ == '__main__':
    args = parser.parse_args()
    if not not args.preset:
        run_preset(args.preset)
    # print(args.preset)