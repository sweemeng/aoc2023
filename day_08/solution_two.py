from utils import parser


def main():
    directions, maps, _ = parser("input.txt")
    print(directions, maps)
    nodes = [i for i in maps.keys() if i.endswith("A")]
    index = 0
    count = 0
    cache = {}
    while True:
        count += 1
        index = index % len(directions)
        direction = directions[index]
        cache_key = (direction, ) + tuple(nodes)
        if cache_key in cache:
            nodes = cache[cache_key]
            index += 1
            continue
        new_nodes = []
        for node in nodes:
            if direction == "L":
                new_nodes.append(maps[node][0])
            else:
                new_nodes.append(maps[node][1])
        check = all(map(lambda x: x.endswith("Z"), new_nodes))
        if check:
            break
        nodes = new_nodes
        cache[cache_key] = nodes
        index += 1

    print(count)


if __name__ == "__main__":
    main()
