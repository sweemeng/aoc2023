import re


def parse_line(line):
    game_id, games = line.split(":")
    games = games.strip().split(";")
    game_id = int(game_id.split(" ")[1])
    return game_id, games


def parse_games(game):
    result = {}
    game_pattern = r"(?P<number>\d+)\s(?P<color>\w+)"
    cubes = re.finditer(game_pattern, game)
    for cube in cubes:
        d = cube.groupdict()
        result[d['color']] = int(d['number'])
    return result
