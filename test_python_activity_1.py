import my_library

assert my_library.count_has_2([2, 3, 4]) == 1
assert my_library.count_has_2([22, 32, 42]) == 3
assert my_library.count_has_2([34, 56, 78]) == 0

print("Tests pass!")