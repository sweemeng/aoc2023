pipe_directions = {
    "|": ((0, 1), (0, -1)),
    "-": ((1, 0), (-1, 0)),
    "L": ((-1, 0), (0, 1)),
    "J": ((-1, 0), (0, -1)),
    "7": ((1, 0), (0, -1)),
    "F": ((1, 0), (0, 1)),
}

adjucent_mask = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]


def make_map(lines):
    maps = {}
    row = 0
    start = None
    for line in lines:
        col = 0
        for char in line:
            maps[(col, row)] = char
            if char == "S":
                start = (col, row)
            col += 1
        row += 1
    return maps, start


def get_endings(maps, point, start):
    endings = []
    pipe = maps[point]
    if pipe in pipe_directions:
        return None
    directions = pipe_directions[pipe]
    for direction in directions:
        new_pos = (point[0] + direction[0], point[1] + direction[1])
        if new_pos == start:
            continue
        if new_pos in maps:
            endings.append(new_pos)
    return endings


def get_second_pipe(maps, start):
    neighbours = []
    for mask in adjucent_mask:
        new_pos = (start[0] + mask[0], start[1] + mask[1])
        if new_pos in maps:
            neighbours.append(new_pos)
    connected = []
    for neighbour in neighbours:
        endings = get_endings(maps, neighbour)
        if start in endings:
            connected.append(neighbour)
    return connected


def main():
    with open("data_test.txt") as f:
        data = f.readlines()
        maps, start = make_map(data)
        print(maps)


if __name__ == "__main__":
    main()
