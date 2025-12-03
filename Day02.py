from numpy.f2py.f2py2e import numpy_version

import result
import numpy as np

with open('input/day02.txt') as f:
    file = f.read().splitlines()

def part1(input):
    input = input[0]
    input = input.split(',')
    invalids = 0

    def split_range(n_range):
        start = n_range[0]
        end = n_range[1]
        if len(start) == len(end):
            return [n_range]
        else:
            ranges = []
            cur = int(start)
            for l in range(len(start), len(end)+1):
                ranges.append([str(cur), str(min(10**l - 1, int(end)))])
                cur = 10**l
            return ranges


    def check_n_range(n_range):
        score = 0
        if len(n_range[0]) % 2 == 1:
            return score
        else:
            start = int(n_range[0])
            end = int(n_range[1])
            current = start
            half = int(len(n_range[0]) / 2)

            if int(start / 10**half) < start - int(start / 10**half) * 10**half:
                current = (int(start / 10**half) + 1) * 10**half

            while int(current / 10**half) < int(end / 10**half):
                score += int(current / 10**half) * 10**half + int(current / 10**half)
                current = (int(current / 10**half) + 1) * 10**half

            if int(current / 10**half) == int(end / 10**half):
                if int(current / 10**half) <= end - int(end / 10**half) *10**half:
                    score += int(current / 10**half) * 10**half + int(current / 10**half)
        return score

    for item in input:
        n_range = item.split('-')
        ranges = split_range(n_range)
        for r in ranges:
            invalids += check_n_range(r)

    answer1 = invalids
    return answer1


def part2(input):

    answer2 = 0
    return answer2

result.print_results(part1, part2, file)
