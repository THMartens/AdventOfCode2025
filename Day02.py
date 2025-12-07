from numpy.f2py.f2py2e import numpy_version

import result
import numpy as np

with open('input/day02.txt') as f:
    file = f.read().splitlines()

def part1(input):
    input = input[0]
    input = input.split(',')
    invalids = 0

    def check_nr(x):
        x_str = str(x)
        d = 2
        if len(x_str) % d == 0:
            n = len(x_str) // d
            pieces = [x_str[i * n:(i + 1) * n] for i in range(d)]
            invalid = len(set(pieces)) == 1
            if invalid:
                return True

        return False

    def check_n_range(r):
        score = 0
        for i in range(int(r[0]),int(r[1])+1):
            if check_nr(i):
                score += i
        return score

    for item in input:
        r = item.split('-')
        invalids += check_n_range(r)

    answer1 = invalids
    return answer1


def part2(input):
    input = input[0]
    input = input.split(',')
    invalids = 0

    def check_nr_all(x):
        x_str = str(x)
        for d in range(1, len(x_str)):
            if len(x_str) % d == 0:
                n = len(x_str) // d
                pieces = [x_str[i * d:(i + 1) * d] for i in range(n)]
                invalid = len(set(pieces)) == 1
                if invalid:
                    return True

        return False

    def check_n_range(r):
        score = 0
        for i in range(int(r[0]), int(r[1]) + 1):
            if check_nr_all(i):
                score += i
        return score

    for item in input:
        r = item.split('-')
        invalids += check_n_range(r)

    answer2 = invalids
    return answer2

result.print_results(part1, part2, file)
