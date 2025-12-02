import numpy as np
import time

def print_results(part1, part2, input):
    p1_start = time.time()
    p1= part1(input)
    p1_end = time.time()
    p2_start = time.time()
    p2= part2(input)
    p2_end = time.time()
    print(f'Part 1: {p1}')
    print(f'Time: {np.round((p1_end - p1_start)*1e3, 2)} ms')
    print(f'Part 2: {p2}')
    print(f'Time: {np.round((p2_end - p2_start)*1e3, 2)} ms')
    return