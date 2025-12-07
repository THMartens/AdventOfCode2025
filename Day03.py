import result
import numpy as np

with open('input/day03.txt') as f:
    file = f.read().splitlines()

def part1(input):

    n_chars = len(input[0])
    values = ['9', '8', '7', '6', '5', '4', '3', '2','1']
    joltage = 0

    def check_first(bank):
        for v in values:
            for i, char in enumerate(bank[:n_chars - 1]):
                if char == v:
                    return i, int(char)

    def check_second(bank, first_index):
        for v in values:
            for char in bank[first_index+1:]:
                if char == v:
                    return int(char)

    for bank in input:
        first_index, first_digit = check_first(bank)
        second_digit = check_second(bank, first_index)
        joltage += first_digit*10 + second_digit

    answer1 = joltage
    return answer1


def part2(input):
    n_chars = len(input[0])
    values = ['9', '8', '7', '6', '5', '4', '3', '2', '1']
    joltage = 0

    def check_first(bank):
        for v in values:
            for i, char in enumerate(bank[:n_chars - 1]):
                if char == v:
                    return i, int(char)

    def check_second(bank, first_index):
        for v in values:
            for char in bank[first_index + 1:]:
                if char == v:
                    return int(char)

    for bank in input:
        first_index, first_digit = check_first(bank)
        second_digit = check_second(bank, first_index)
        joltage += first_digit * 10 + second_digit

    answer2 = joltage

    return answer2

result.print_results(part1, part2, file)
