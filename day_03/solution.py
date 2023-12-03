import string

from utils import get_neighbors, is_valid


def make_map(file_name):
    line_no = 0
    schematic = {}
    part_numbers = {}

    with open(file_name, "r") as f:
        data = f.readlines()
        # These are them value to be overriden
        part_number = ""
        part_positions = []
        for line in data:
            line = line.strip()
            for idx, char in enumerate(line):
                if char not in string.digits:
                    if part_number:
                        if part_number not in part_numbers:
                            part_numbers[part_positions[0]] = part_number
                    part_number = ""
                    part_positions = []
                else:
                    part_number += char
                    part_positions.append((idx, line_no))
                schematic[(idx, line_no)] = char
            line_no += 1
    return schematic, part_numbers


def get_number_coordinates(schematic, key, value):
    points = []
    for i in range(len(value)):
        points.append((key[0] + i, key[1]))
    return points


# not 1151039
# not 1169240
# not 1382231
def main():
    schematics, part_numbers = make_map("day_03/data_test.txt")
    results = []
    result_set = set()
    for part_number in part_numbers:
        part_positions = get_number_coordinates(schematics, part_number, part_numbers[part_number])
        neighbors = get_neighbors(schematics, part_positions)
        if is_valid(neighbors):
            results.append(int(part_numbers[part_number]))
            result_set.add(int(part_numbers[part_number]))
    print(sum(result_set))
    print(sum(results))
    print(len(results))
    print(len(result_set))


if __name__ == "__main__":
    main()
