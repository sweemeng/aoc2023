from utils import parser


def main():
    directions, maps, _ = parser("input.txt")
    print(directions, maps)
    node = "AAA"
    count = 0
    index = 0
    while True:
        index = index % len(directions)
        direction = directions[index]
        if direction == "L":
            node = maps[node][0]
        else:
            node = maps[node][1]
        count += 1
        index += 1
        if node == "ZZZ":
            break
    print(count)


if __name__ == "__main__":
    main()
