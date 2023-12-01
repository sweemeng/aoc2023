digits_tree = {
    "o": ["on"],
    "on": ["one"],
    "one": 1,
    "t": ["tw", "th"],
    "tw": ["two"],
    "two": 2,
    "th": ["thr"],
    "thr": ["thre"],
    "thre": ["three"],
    "three": 3,
    "f": ["fo", "fi"],
    "fo": ["fou"],
    "fou": ["four"],
    "four": 4,
    "fi": ["fiv"],
    "fiv": ["five"],
    "five": 5,
    "s": ["si", "se"],
    "si": ["six"],
    "six": 6,
    "se": ["sev"],
    "sev": ["seven"],
    "seve": ["seven"],
    "seven": 7,
    "e": ["ei"],
    "ei": ["eig"],
    "eig": ["eigh"],
    "eigh": ["eight"],
    "eight": 8,
    "n": ["ni"],
    "ni": ["nin"],
    "nin": ["nine"],
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}

def main():
    results = []
    count = 0
    with open("input.txt", "r") as f:
        data = f.readlines()
        for line in data:
            count += 1
            digits = parse(line)
            print(line)
            print(digits)
            value = 10 * digits[0] + digits[-1]
            print(value)
            results.append(value)
    print(sum(results))
    print(count)


def parse(line):
    line = line.strip()
    result = []
    head = 0
    tail = 0
    while tail <= len(line):
        if head == tail:
            tail += 1
        if head > tail:
            tail = head
            continue
        if line[head:tail] in digits_tree:
            if isinstance(digits_tree[line[head:tail]], int):
                result.append(digits_tree[line[head:tail]])
                head += 1
            else:
                tail += 1
        else:
            head += 1

    return result


if __name__ == "__main__":
    main()