import itertools
import string

from day_03.utils import get_neighbors, is_valid


def make_map(file_name):
    line_no = 0
    schematic = {}

    with open(file_name, "r") as f:
        data = f.readlines()
        for line in data:
            line = line.strip()
            for idx, char in enumerate(line):
                schematic[(idx, line_no)] = char
            line_no += 1
    return schematic


def make_number_index(schematic):
    part_numbers = {}
    max_length = max(i for i, _ in schematic.keys()) + 1
    print(max_length)
    point = None
    for i, j in itertools.product(range(max_length), repeat=2):
        if schematic[(j, i)] in string.digits:
            if not point:
                point = (j, i)
                part_numbers[point] = schematic[(j, i)]
            else:
                part_numbers[point] += schematic[(j, i)]
        else:
            point = None
    return part_numbers


def get_number_coordinates(key, value):
    points = []
    for i in range(len(value)):
        points.append((key[0] + i, key[1]))
    return points


# not 1151039
# not 1169240
# not 1382231
def main():
    schematics = make_map("day_03/input.txt")
    results = []
    part_numbers = make_number_index(schematics)
    result_set = set()
    for part_number in part_numbers:
        part_positions = get_number_coordinates(part_number, part_numbers[part_number])
        neighbors = get_neighbors(schematics, part_positions)
        if is_valid(neighbors):
            results.append(int(part_numbers[part_number]))
            result_set.add(int(part_numbers[part_number]))
    print(part_numbers)
    print(sum(result_set))
    print(sum(results))
    print(len(results))
    print(len(result_set))


if __name__ == "__main__":
    main()
