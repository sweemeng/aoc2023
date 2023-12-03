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
