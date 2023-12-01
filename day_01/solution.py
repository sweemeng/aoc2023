import string

digits = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
]

def main():
    values = []
    with open("data_test2.txt", "r") as f:
        data = f.read().splitlines()
    for line in data:
        d = [i for i in line if i in string.digits]
        value = 10 * int(d[0]) + int(d[-1])
        values.append(value)
    print(sum(values))


if __name__ == "__main__":
    main()
