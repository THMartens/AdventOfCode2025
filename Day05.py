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
    fresh_ids, ingredients = input.split('\n\n')
    fresh_ids = fresh_ids.splitlines()
    fresh_ids = [list(map(int, i.split('-'))) for i in fresh_ids]

    def trim_range(new_range, old_max):
        if old_max > new_range[1]:
            return []
        else:
            return [max(new_range[0], old_max + 1), new_range[1]]

    fresh_ranges = [[0,0]]
    for r in sorted(fresh_ids):
        trimmed_r = trim_range(r, fresh_ranges[-1][1])
        if trimmed_r:
            fresh_ranges.append(trimmed_r)


    fresh_ingredients = 0
    for fr in fresh_ranges:
        fresh_ingredients += fr[1] - fr[0] + 1


    fresh_ingredients = fresh_ingredients - 1
    answer2 = fresh_ingredients
    return answer2

result.print_results(part1, part2, file)
