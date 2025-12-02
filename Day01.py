import result
import numpy as np

with open('input/day01.txt') as f:
    file = f.read().splitlines()

def part1(input):

    def turn_dial(current, turn):
        if turn.startswith('L'):
            return (current - int(turn[1:])) % 100

        else:
            return (current + int(turn[1:])) % 100

    dial = 50
    zeros = 0
    for turn in input:
        if dial == 0:
            zeros += 1
        dial = turn_dial(dial, turn)

    answer1 = zeros
    return answer1


def part2(input):
    def turn_dial(current, turn):
        if turn.startswith('L'):
            new_dial = (current - int(turn[1:])) % 100
            if current == 0:
                current = 100
            zeros_count = int(-1 * np.floor(((current - int(turn[1:])) / 100) - 0.001))
            return  new_dial, zeros_count

        else:
            new_dial = (current + int(turn[1:])) % 100
            zeros_count = int(np.floor((current + int(turn[1:])) / 100))
            return new_dial, zeros_count

    dial = 50
    zeros = 0
    for turn in input:
        dial, zeros_count = turn_dial(dial, turn)
        zeros += zeros_count

    answer2 = zeros
    return answer2

result.print_results(part1, part2, file)
