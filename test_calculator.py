from calculator import add

assert add("") == 0
assert add("1") == 1
assert add("1,5") == 6
assert add("1\n2,3") == 6

