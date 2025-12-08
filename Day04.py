import result
import numpy as np

with open('input/day04.txt') as f:
    file = f.read().splitlines()

def part1(input):

    def check_surroundings(arr,i,j):
        count = 0
        offsets = [(-1, -1), (-1, 0), (-1, 1),
                   ( 0, -1),          ( 0, 1),
                   ( 1, -1), ( 1, 0), ( 1, 1)]

        for o_x, o_y in offsets:
            if -1 < i + o_x < len(arr) and -1 < j + o_y < len(arr):
                if arr[i+o_x][j+o_y] == '@':
                    count += 1
        if count < 4:
            return True
        else:
            return False

    paper_rolls = 0
    for i, row in enumerate(input):
        for j, char in enumerate(row):
            if char == '@':
                paper_rolls += check_surroundings(input, i, j)

    answer1 = paper_rolls
    return answer1


def part2(input):

    answer2 = 0
    return answer2

result.print_results(part1, part2, file)
