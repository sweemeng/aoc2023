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
                            part_numbers[part_number] = []
                        part_numbers[part_number].append(part_positions)
                    part_number = ""
                    part_positions = []
                else:
                    part_number += char
                    part_positions.append((idx, line_no))
                schematic[(idx, line_no)] = char
            line_no += 1
    return schematic, part_numbers


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
    schematics, part_numbers = make_map("day_03/input.txt")
    results = []
    for part_number in part_numbers:
        print("part number:", part_number)
        for area in part_numbers[part_number]:
            neighbors = get_neighbors(schematics, area)
            if is_valid(neighbors):
                results.append(int(part_number))
    print(sum(results))
    print(sum(set(results)))
    print(len(set(results)))


if __name__ == "__main__":
    main()
