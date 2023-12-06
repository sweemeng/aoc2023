from functools import reduce

test_data = [
    (7, 9),
    (15, 40),
    (30, 200)
]

real_data = [
    (41, 249),
    (77, 1362),
    (70, 1127),
    (96, 1011)
]


def get_distances(duration, current_distance):
    distance_func = lambda t, d: t * (d - t)
    records = []
    for t in range(duration):
        distance = distance_func(t, duration)
        if distance > current_distance:
            records.append((t, distance))
    return records


def stringy_records(data):
    duration = "".join([str(t) for t, _ in data])
    distance = "".join([str(d) for _, d in data])
    return int(duration), int(distance)


def main():

    test_approaches = []
    for duration, current_distance in test_data:
        records = get_distances(duration, current_distance)
        test_approaches.append(len(records))
    result = reduce(lambda x, y: x * y, test_approaches)
    print(result)

    approaches = []
    for duration, current_distance in real_data:
        records = get_distances(duration, current_distance)
        approaches.append(len(records))
    result = reduce(lambda x, y: x * y, approaches)
    print(result)

    print("Round two")
    test_duration, test_distance = stringy_records(test_data)
    records = get_distances(test_duration, test_distance)
    print(len(records))

    duration, distance = stringy_records(real_data)
    records = get_distances(duration, distance)
    print(len(records))


if __name__ == "__main__":
    main()
