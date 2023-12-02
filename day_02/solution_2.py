from utils import parse_line, parse_games


def main():
    data_file = "input.txt"
    with open(data_file, 'r') as f:
        lines = f.readlines()

    results = []
    for line in lines:
        minimum_cubes = {
            "red": 0,
            "blue": 0,
            "green": 0,
        }
        game_id, games = parse_line(line)
        print(game_id)
        for game in games:
            cubes = parse_games(game)
            for key, value in cubes.items():
                if value > minimum_cubes[key]:
                    minimum_cubes[key] = value
        print(minimum_cubes)
        power = minimum_cubes['red'] * minimum_cubes['blue'] * minimum_cubes['green']
        results.append(power)
    print(results)
    print(sum(results))


if __name__ == "__main__":
    main()
