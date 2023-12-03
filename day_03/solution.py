import string


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


def get_neighbors(schematic, part_positions):
    neighbor_positions = get_neighbors_positions(part_positions)
    neighbors = []
    for x, y in neighbor_positions:
        value = schematic.get((x, y), None)
        if value:
            neighbors.append(schematic[(x, y)])
    return neighbors


def get_neighbors_positions(part_positions):
    mask = [
        (-1, -1),
        (0, -1),
        (1, -1),
        (-1, 0),
        (1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
    ]
    results = set()

    for x, y in part_positions:
        for dx, dy in mask:
            point = (x + dx, y + dy)
            if point not in part_positions:
                results.add((x + dx, y + dy))
    return list(results)


def is_valid(neighbors):
    invalid_values = "."
    results = []
    for neighbor in neighbors:
        if neighbor in invalid_values:
            results.append(False)
        else:
            results.append(True)
    return any(results)


def print_schematic(schematic, max_length=140):
    for y in range(max_length):
        for x in range(max_length):
            print(schematic[(x, y)], end="")
        print()


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
