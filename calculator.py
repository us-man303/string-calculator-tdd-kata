import re

class NegativeNumberException(Exception):
    pass

def add(numbers: str) -> int:
    if numbers == "":
        return 0
    
    delimiters = [",", "\n"]

    # Check for custom delimiter
    if numbers.startswith("//"):
        delimiter_section_end = numbers.index("\n")
        delimiter_part = numbers[2:delimiter_section_end]

        # Handle multiple delimiters or single delimiter of any length
        if delimiter_part.startswith("[") and delimiter_part.endswith("]"):
            delimiters = re.findall(r"\[([^\]]+)\]", delimiter_part)
        else:
            delimiters = [delimiter_part]
        
        numbers = numbers[delimiter_section_end + 1:]

    # Create regex pattern to split by any of the delimiters
    delimiter_pattern = "|".join(map(re.escape, delimiters))
    num_list = re.split(delimiter_pattern, numbers)

    # Convert numbers to integers and check for negatives
    negatives = [int(num) for num in num_list if num and int(num) < 0]
    if negatives:
        raise NegativeNumberException(f"negative numbers not allowed: {', '.join(map(str, negatives))}")

    # Ignore numbers greater than 1000 and sum the rest
    num_list = [int(num) for num in num_list if num and int(num) <= 1000]

    return sum(num_list)

