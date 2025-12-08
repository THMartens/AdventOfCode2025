import result
import numpy as np

with open('input/day05.txt') as f:
    file = f.read()

def part1(input):
    fresh_ids, ingredients = input.split('\n\n')
    fresh_ids = fresh_ids.splitlines()
    fresh_ids = [list(map(int, i.split('-'))) for i in fresh_ids]
    ingredients = [int(i) for i in ingredients.splitlines()]

    fresh_ingredients = 0
    for ingredient in ingredients:
        for r in fresh_ids:
            if ingredient >= r[0] and ingredient <= r[1]:
                fresh_ingredients += 1
                break


    answer1 = fresh_ingredients
    return answer1


def part2(input):

    answer2 = 0
    return answer2

result.print_results(part1, part2, file)
