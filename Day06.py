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

    def column_empty(input, i):
        for j in range(len(input) - 1):
            if input[j][-i] != ' ':
                return False
        return True

    def find_number(input, i):
        nr = ''
        for j in range(len(input) - 1):
            nr += input[j][-i]
        return int(nr)


    operations = input[-1].split()
    operation = operations[-1]
    prob_nr = 0
    total = 0
    if operation == '+':
        prob_total = 0
    elif operation == '*':
        prob_total = 1

    for i in range(1, len(input[0]) + 1):
        if column_empty(input, i):
            prob_nr += 1
            total += prob_total
            operation = operations[-prob_nr - 1]
            if operation == '+':
                prob_total = 0
            elif operation == '*':
                prob_total = 1
        else:
            nr = find_number(input, i)
            if operation == '+':
                prob_total += nr
            elif operation == '*':
                prob_total *= nr

    total += prob_total

    answer2 = total
    return answer2

result.print_results(part1, part2, file)
