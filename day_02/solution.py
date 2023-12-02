from day_02.utils import parse_line, parse_games

CUBE_NUMBER = {
    "red": 12,
    "blue": 14,
    "green": 13,
}


def main():
    possible_set = set()
    data_file = "input.txt"
    with open(data_file, 'r') as f:
        lines = f.readlines()
    for line in lines:
        game_id, games = parse_line(line)
        print(game_id)
        possible = True
        for game in games:
            cubes = parse_games(game)
            for key, value in cubes.items():
                print(key, value, CUBE_NUMBER[key])
                if value > CUBE_NUMBER[key]:
                    possible = False
        if possible:
            possible_set.add(game_id)

    print(possible_set)
    print(sum(possible_set))


if __name__ == "__main__":
    main()

