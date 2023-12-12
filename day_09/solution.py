def get_diffs(data):
    # start with one, then go to the end, make a list of diff
    results = []
    for i in range(1, len(data)):
        results.append(data[i] - data[i-1])
    return results


def process_numbers(line):
    results = []
    current = line
    results.append(current)
    while True:
        current = get_diffs(current)
        print(current)
        check = all(map(lambda x: x == 0, current))
        results.append(current)
        if check:
            break
    return results


def predict_next(datas):
    numbers = []
    diff = 0
    for i in datas:
        numbers.append(i[-1])
    return sum(numbers)


def predict_past(datas):
    diff = 0

    for i in range(len(datas) - 1, -1, -1):
        data_list = datas[i]
        print("processing:", data_list[0])
        diff = data_list[0] - diff
        print("currently:", diff)
    return diff


def main():
    with open("input.txt") as f:
        data = f.readlines()
        all_results = []
        for line in data:
            print(line)
            line = line.strip()
            numbers = [int(i) for i in line.split(" ")]
            diffs = process_numbers(numbers)
            result = predict_next(diffs)
            print(result)
            all_results.append(result)
        print(sum(all_results))

        print("part 2 predict past")
        all_results = []
        for line in data:
            print(line)
            line = line.strip()
            numbers = [int(i) for i in line.split(" ")]
            diffs = process_numbers(numbers)
            result = predict_past(diffs)
            print(result)
            all_results.append(result)
        print(sum(all_results))



if __name__ == "__main__":
    main()

