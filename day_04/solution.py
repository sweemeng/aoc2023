import re


def parse(file_name):
    results = []
    with open(file_name, "r") as f:
        data = f.readlines()
        for line in data:
            game_id, winning, my_number = parse_line(line)
            results.append((game_id, winning, my_number))
            overlap = winning.intersection(my_number)
            if overlap:
                print(game_id, overlap)
                print(len(overlap))
    return results


def parse_line(line):
    game, numbers = line.split(":")
    winning_str, my_number_str = numbers.split("|")
    game = game.strip()
    winning = parse_numbers(winning_str)
    my_number = parse_numbers(my_number_str)

    return game, winning, my_number


def parse_numbers(numbers):
    numbers = re.findall("\d+", numbers)
    return set(int(i) for i in numbers)


def main():
    results = parse("input.txt")
    scores = []
    cards = {}
    key_order = []
    overlaps = {}
    for game_id, winning, my_number in results:
        overlap = winning.intersection(my_number)
        print(game_id, overlap)
        overlaps[game_id] = overlap
        cards[game_id] = {
            "winning": winning,
            "my_number": my_number
        }
        key_order.append(game_id)
        if overlap:

            print("overlap:", len(overlap))
            score_list = [2 ** i for i in range(len(overlap))]
            print(score_list)
            print("score:", score_list[-1])
            scores.append(score_list[-1])
        else:
            print(game_id, "no overlap")
    print(sum(scores))

    print("round 2")
    copies = {key: 1 for key in cards.keys()}
    for index in range(len(key_order)):
        key = key_order[index]
        overlap = overlaps[key]
        length = len(overlap)
        num_copy = copies[key]
        sublist = key_order[index + 1:index + length + 1]
        for sub in sublist:
            copies[sub] += num_copy

    print(copies)
    print(sum(copies.values()))


if __name__ == "__main__":
    main()
