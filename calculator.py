def add(numbers: str) -> int:
    if numbers == "":
        return 0
    
    if numbers.startswith("//"):
        delimiter_index = numbers.index("\n")
        delimiter = numbers[2:delimiter_index]
        numbers = numbers[delimiter_index + 1:]
        num_list = map(int, numbers.split(delimiter))
    else:
        numbers = numbers.replace("\n", ",")
        num_list = map(int, numbers.split(','))
    
    return sum(num_list)

print(add("//;\n1;2"))
