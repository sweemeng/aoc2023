import re
from math import inf


def parse_file(file_path):
    results = {}
    steps = []
    with open(file_path, 'r') as f:
        data = f.readlines()
    print(data[0])
    seed_line = data[0].split(":")[1].strip().split(" ")
    print(seed_line)
    seeds = [int(x) for x in seed_line]
    working_data = None
    for line in data[1:]:
        if not line.strip():
            continue
        if not re.search(r"^\d", line):
            source_keys = re.findall(r"\w+", line)
            source_key = source_keys[2]
            steps.append(source_key)
            results[source_key] = {}
            working_data = results[source_key]
            continue
        line = line.strip()
        dest_str, source_str, step_str = line.split(" ")
        dest = int(dest_str)
        source = int(source_str)
        step = int(step_str)
        working_data[source] = (dest, step)
    return seeds, results, steps


def get_map_data(data, source):
    result = None
    for key in data:
        dest, step = data[key]

        if source > key:
            diff = source - key
            if diff > step:
                continue
            result = dest + diff
    if not result:
        return source
    return result


def make_seed_map(seed, data, steps):
    result = {"seed": seed}
    value = seed
    for step in steps:
        value = get_map_data(data[step], value)
        result[step] = value
    return result


def get_actual_start(data, seed):
    keys = sorted(data.keys())
    for key in keys:
        if key > seed:
            return key - 1
    return None


def get_map_data_ranges(data, seed, ranges):
    # Let's return list of tuple of 2 with (dest, range)
    groups = []
    keys = sorted(data.keys())
    index = get_actual_start(data, seed)
    start = seed
    while True:
        if keys[index] > seed + ranges:
            break
        diff = start - keys[index]
        dest, step = data[keys[index]]
        groups.append((dest + diff, step - diff))
        start = keys[index] + step
        index += 1
        if keys[index] != start:
            groups.append((start, keys[index] - start))
            start = keys[index]
            index += 1

    return groups



def main():
    # TODO: Get seeds first
    # then use step to direct which direction, start from first item
    # use get map data to get the next key, repeat until no more steps
    seeds, data, steps = parse_file("input.txt")
    min_location = inf
    for seed in seeds:
        maps = make_seed_map(seed, data, steps)
        if min_location > maps["location"]:
            min_location = maps["location"]
    print(min_location)

    print("part 2")
    # group seeds into a list of tuple of 2 items
    seeds_group = [
        (seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)
    ]

    min_location = inf
    for seed, ranges in seeds_group:
        for i in range(ranges):
            new_seed = seed + i
            maps = make_seed_map(new_seed, data, steps)
            if min_location > maps["location"]:
                min_location = maps["location"]
    print(min_location)


if __name__ == "__main__":
    main()
