import result
import numpy as np

with open('input/day08.txt') as f:
    file = f.read().splitlines()


def part1(input):

    N_connects = 1000

    def find_min_and_update(distmap, circuits):
        idx = np.argmin(distmap)
        coords = np.unravel_index(idx, distmap.shape)
        distmap[coords] = 1e10
        connected = False

        for circuit in circuits:
            if coords[0] in circuit:
                connected = True
                if coords[1] in circuit:
                    break
                else:
                    for circuit2 in circuits:
                        if coords[1] in circuit2:
                            combined = circuit | circuit2
                            circuits.remove(circuit)
                            circuits.remove(circuit2)
                            circuits.append(combined)
                            break
                    circuit.add(coords[1])
                    break

            elif coords[1] in circuit:
                connected = True
                circuit.add(coords[0])
                break

        else:
            circuits.append({coords[0], coords[1]})

        return distmap, circuits

    input = [[int(j) for j in i.split(',')] for i in input]

    distmap = np.zeros((len(input), len(input)))
    for x in range(len(input)):
        for y in range(len(input)):
            if x >= y:
                distmap[x,y] = 1e10
            else:
                distmap[x,y] = ((input[x][0] - input[y][0]) **2 +
                                (input[x][1] - input[y][1]) **2 +
                                (input[x][2] - input[y][2]) **2)

    circuits = []

    for _ in range(N_connects):
        distmap, circuits = find_min_and_update(distmap, circuits)

    prod = sorted(circuits, key=len, reverse=True)
    print(len(prod[0]), len(prod[1]), len(prod[2]))
    answer1 = len(prod[0]) * len(prod[1]) * len(prod[2])
    return answer1


def part2(input):

    answer2 = 0
    return answer2

result.print_results(part1, part2, file)