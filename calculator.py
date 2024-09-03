def add(numbers: str) -> int:
    if numbers == "":
        return 0
    else:
        numbers = numbers.replace("\n", ",")
        num_list = map(int, numbers.split(','))
        return sum(num_list)
