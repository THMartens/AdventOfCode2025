import result
import numpy as np

with open('input/day07.txt') as f:
    file = f.read().splitlines()

def part1(input):
    beams = []
    splitters = set()
    for i, char in enumerate(input[0]):
        if char == 'S':
            beams.append([0,i])
            break

    def progress(input, beam, beams, splitters):
        if input[beam[0] + 1][beam[1]] == '.':
            beams.append([beam[0] + 1, beam[1]])
            return beams, splitters

        if input[beam[0] + 1][beam[1]] == '^':
            if (beam[0] + 1) + beam[1] * 1j in splitters:
                return beams, splitters
            else:
                splitters.add((beam[0] + 1) + beam[1] * 1j)
                beams.append([beam[0] + 2, beam[1] - 1])
                beams.append([beam[0] + 2, beam[1] + 1])
                return beams, splitters


    while len(beams) > 0:
        beam = beams.pop()
        if beam[0] < len(input) - 1:
            beams, splitters = progress(input, beam, beams, splitters)

    nr_splitters = len(splitters)

    answer1 = nr_splitters
    return answer1


def part2(input):

    nr_timelines = 0

    def add_splitter(input, splitters, i, cur_row):
        j = cur_row + 1
        while j < len(input) - 1:
            if (j, i-1) in splitters:
                splitters[(cur_row, i)] = splitters[(j, i-1)]
                break
            j += 1

        if j == len(input) - 1:
            splitters[(cur_row, i)] = 1

        j = cur_row + 1
        while j < len(input) - 1:
            if (j, i+1) in splitters:
                splitters[(cur_row, i)] += splitters[(j, i+1)]
                break
            j += 1

        if j == len(input) - 1:
            splitters[(cur_row, i)] += 1

        return splitters


    splitters = {}
    for r in reversed(range(len(input) - 1)):

        for i, char in enumerate(input[r]):
            if char == '^' or char == 'S':
                splitters = add_splitter(input, splitters, i, r)

    for k, char in enumerate(input[0]):
        if char == 'S':
            nr_timelines = splitters[(0, k)]
            break

    print(splitters)
    answer2 = nr_timelines
    return answer2

result.print_results(part1, part2, file)
