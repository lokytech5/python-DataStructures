letters = ["a", "b", "c", "d", "e", "f", "ad"]

# Add items to a list

# Add items to the beginning of the list
letters.insert(0, "y")

# Remove items form the list
# The pop method only remove one item from the list
letters.pop()
# letters.remove("e")
# the del method remove a range of items from the list
del letters[0:3]
letters.clear()
print(letters)
