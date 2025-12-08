import result
import numpy as np

with open('input/day03.txt') as f:
    file = f.read().splitlines()

def part1(input):
    n_chars = len(input[0])
    active_bats = 2
    values = ['9', '8', '7', '6', '5', '4', '3', '2', '1']
    joltage = 0

    def check_bank(bank, bat_nr, prev_index):
        for v in values:
            for i, char in enumerate(bank[prev_index+1:n_chars - (active_bats - bat_nr) + 1]):
                if char == v:
                    return i + prev_index + 1, v

    for bank in input:
        prev_index = -1
        digits = []
        for bat_nr in range(active_bats):
            prev_index, digit = check_bank(bank, bat_nr, prev_index)
            digits.append(digit)

        joltage += int(''.join(digits))

    answer1 = joltage

    return answer1


def part2(input):
    n_chars = len(input[0])
    active_bats = 12
    values = ['9', '8', '7', '6', '5', '4', '3', '2', '1']
    joltage = 0

    def check_bank(bank, bat_nr, prev_index):
        for v in values:
            for i, char in enumerate(bank[prev_index + 1:n_chars - (active_bats - bat_nr) + 1]):
                if char == v:
                    return i + prev_index + 1, v

    for bank in input:
        prev_index = -1
        digits = []
        for bat_nr in range(active_bats):
            prev_index, digit = check_bank(bank, bat_nr, prev_index)
            digits.append(digit)

        joltage += int(''.join(digits))

    answer2 = joltage

    return answer2

result.print_results(part1, part2, file)
