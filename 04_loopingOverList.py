letters = ["a", "b", "c", "d", "e", "f", "g"]
matrix = [[0, 1], [2, 3]]
items = (0, "a")
index, letter = items
for index, letter in enumerate(letters):
    print(index, letter)