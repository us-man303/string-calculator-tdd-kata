class NegativeNumberException(Exception):
    pass

def add(numbers: str) -> int:
    if numbers == "":
        return 0
    
    if numbers.startswith("//"):
        delimiter_index = numbers.index("\n")
        delimiter = numbers[2:delimiter_index]
        numbers = numbers[delimiter_index + 1:]
        num_list = numbers.split(delimiter)
    else:
        numbers = numbers.replace("\n", ",")
        num_list = numbers.split(',')
    
    negatives = [int(num) for num in num_list if int(num) < 0]
    if negatives:
        raise NegativeNumberException(f"negative numbers not allowed: {', '.join(map(str, negatives))}")

    num_list = map(int, num_list)
    return sum(num_list)
