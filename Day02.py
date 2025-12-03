import result
import numpy as np

with open('input/day02.txt') as f:
    file = f.read().splitlines()

def part1(input):
    input = input[0]
    input = input.split(',')
    invalids = 0

    def check_id(id, length):
        return str(id)[:int(length / 2)] == str(id)[int(length / 2):]

    for item in input:
        string_start, string_end = item.split('-')
        start = int(string_start)
        end = int(string_end)

        if len(string_start) == len(string_end) and len(string_start) % 2 == 0:
            length = len(string_start)

            for x in range(start, end + 1):
                if check_id(x, length):
                    invalids += x

        elif len(string_start) != len(string_end) and len(string_start) % 2 == 0:
            length = len(string_start)
            for x in range(start, 10**length):
                if check_id(x, length):
                    invalids += x

        elif len(string_start) != len(string_end) and len(string_end) % 2 == 0:
            length = len(string_end)
            for x in range(10**(length-1), end):
                if check_id(x, length):
                    invalids += x

        elif len(string_start) != len(string_end):
            raise Exception('Ranges span more than 1 order of magnitude!')

    answer1 = invalids
    return answer1


def part2(input):

    answer2 = 0
    return answer2

result.print_results(part1, part2, file)
