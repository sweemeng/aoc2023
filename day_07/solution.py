from collections import Counter
from functools import cmp_to_key, partial

card_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
joker_ranks = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
# Count of card with biggest number first, with a total of each tuple is 5
pattern_ranks = [(1, 1, 1, 1, 1), (2, 1, 1, 1), (2, 2, 1), (3, 1, 1), (3, 2), (4, 1), (5,), ]


def resolve_tie(cards_one, cards_two, ranks=None):
    if ranks is None:
        ranks = card_ranks
    for i in range(5):
        card_one = ranks.index(cards_one[i])
        card_two = ranks.index(cards_two[i])
        if card_two > card_one:
            return -1
        elif card_one > card_two:
            return 1
    return 0


def main():
    ranks = []
    bids = {}
    patterns = {key: [] for key in pattern_ranks}
    with open("input.txt") as f:
        data = f.read().splitlines()
        for line in data:
            cards, bid_str = line.split(" ")
            bid = int(bid_str)
            bids[cards] = bid
            count = Counter(cards)
            card_counts = tuple(sorted(count.values(), reverse=True))
            patterns[card_counts].append(cards)
    rank = 0
    for key in patterns:
        ordered_cards = sorted(patterns[key], key=cmp_to_key(resolve_tie))
        for cards in ordered_cards:
            rank += 1
            ranks.append((rank, cards, bids[cards]))
    total = 0
    for rank, cards, bid in ranks:
        # print(f"{rank} {cards} {bid}")
        total += bid * rank
    print(total)

    print("Round two")
    ranks = []
    patterns = {key: [] for key in pattern_ranks}
    # because we already store the cards there
    # Not 248618050
    # 248750248
    for cards in bids:
        count = Counter(cards)
        if "J" in count and count["J"] != 5:
            jc = count["J"]
            del count["J"]
            max_count = max(count, key=lambda c: count[c])

            count[max_count] += jc

        card_counts = tuple(sorted(count.values(), reverse=True))
        patterns[card_counts].append(cards)
    rank = 0
    for key in patterns:
        j_resolve_tile = partial(resolve_tie, ranks=joker_ranks)
        ordered_cards = sorted(patterns[key], key=cmp_to_key(j_resolve_tile))
        print(key, ordered_cards)
        for cards in ordered_cards:
            rank += 1
            ranks.append((rank, cards, bids[cards]))
    total = 0
    for rank, cards, bid in ranks:
        # print(f"{rank} {cards} {bid}")
        total += bid * rank
    print(total)


if __name__ == "__main__":
    main()
