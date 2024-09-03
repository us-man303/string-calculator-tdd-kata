from calculator import add, NegativeNumberException

assert add("") == 0
assert add("1") == 1
assert add("1,5") == 6
assert add("1\n2,3") == 6
assert add("//;\n1;2") == 3

try:
    add("-1,2,-3")
except NegativeNumberException as e:
    assert str(e) == "negative numbers not allowed: -1,-3"
