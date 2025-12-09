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
    beams = []
    nr_timelines = 1
    for i, char in enumerate(input[0]):
        if char == 'S':
            beams.append([0, i])
            break

    def progress(input, beam, beams,  nr_timelines):
        if input[beam[0] + 1][beam[1]] == '.':
            beams.append([beam[0] + 1, beam[1]])
            return beams, nr_timelines

        if input[beam[0] + 1][beam[1]] == '^':
            nr_timelines += 1
            beams.append([beam[0] + 2, beam[1] - 1])
            beams.append([beam[0] + 2, beam[1] + 1])
            return beams, nr_timelines

    while len(beams) > 0:
        beam = beams.pop()
        if beam[0] < len(input) - 1:
            beams, nr_timelines = progress(input, beam, beams, nr_timelines)


    answer2 = nr_timelines
    return answer2

result.print_results(part1, part2, file)
