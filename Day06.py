import result
import numpy as np

with open('input/day06.txt') as f:
    file = f.read().splitlines()

def part1(input):
    import math
    problems = np.zeros((len(input[0].split()),len(input)-1), dtype=int)
    for i, line in enumerate(input[:len(input)-1]):
        problems[:,i] = line.split()

    total = 0
    for j, operation in enumerate(input[-1].split()):
        if operation == '+':
            total += sum(problems[j][:])
        elif operation == '*':
            total += math.prod(problems[j][:])

    answer1 = total
    return answer1


def part2(input):

    answer2 = 0
    return answer2

result.print_results(part1, part2, file)
