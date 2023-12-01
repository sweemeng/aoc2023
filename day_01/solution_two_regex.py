import re
import string


def main():
    patterns = r"one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9"
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    with open("input.txt", "r") as f:
        data = f.read().splitlines()
    results = []
    for line in data:
        result = []
        print(line)
        for i in range(len(line)):
            m = re.search(patterns, line[i:])
            if not m:
                continue
            r = m.group(0)
            if r in digits:
                result.append(digits.index(r)+1)
            if r in string.digits:
                result.append(int(r))
        print(result)
        value = 10 * result[0] + result[-1]
        results.append(value)
    print(sum(results))


if __name__ == "__main__":
    main()