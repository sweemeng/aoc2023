import re


def parser(input_file):
    maps = {}
    with open(input_file, "r") as f:
        data = f.read().splitlines()
        directions = data[0]
        start = None
        for line in data[1:]:
            if not line:
                continue

            nodes = re.findall(r"\w+", line)
            if not start:
                start = nodes[0]
            maps[nodes[0]] = (nodes[1], nodes[2])
    return directions, maps, start
