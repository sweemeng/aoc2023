import re

from utils import get_neighbors_positions


def make_number_index(line, row):
    matches = re.finditer(r"\d+", line)
    numbers = {}
    for match in matches:
        span = match.span()
        numbers[(span[0], row)] = match.group(0)
    return numbers


def make_number_indexes(data):
    numbers = {}
    for row, line in enumerate(data):
        numbers.update(make_number_index(line, row))
    return numbers


def make_symbol_index(line, row):
    matches = re.finditer(r"[@*/&#%+=$-]", line)
    symbols = {}
    for match in matches:
        span = match.span()
        symbols[(span[0], row)] = match.group(0)
    return symbols


def get_number_coordinates(key, value):
    points = []
    for i in range(len(value)):
        points.append((key[0] + i, key[1]))
    return points


def make_symbol_indexes(data):
    symbols = {}
    for row, line in enumerate(data):
        symbols.update(make_symbol_index(line, row))
    return symbols


def main():
    with open("day_03/input.txt", "r") as f:
        data = f.readlines()
    numbers = make_number_indexes(data)
    symbols = make_symbol_indexes(data)
    gears = {point: [] for (point, gear) in symbols.items() if gear == "*"}
    results = []
    for number in numbers:
        number_positions = get_number_coordinates(number, numbers[number])
        neighbor = get_neighbors_positions(number_positions)
        for n in neighbor:
            value = symbols.get(n)
            if value == "*":
                gears[n].append(int(numbers[number]))
    for key, values in gears.items():
        if len(values) == 2:
            results.append(values[0] * values[1])
    print(sum(results))


if __name__ == "__main__":
    main()