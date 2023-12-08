import re

def parser(input_file):
    maps = {}
    with open(input_file, "r") as f:
        data = f.read().splitlines()
        directions = data[0]
        for line in data[1:]:
            if not line:
                nodes = re.findall(r"\w+", line)
                maps[nodes[0]] = (nodes[1], nodes[2])
    return directions, maps


def main():
    directions, maps = parser("data_test.txt")
    print(directions)
    print(maps)
