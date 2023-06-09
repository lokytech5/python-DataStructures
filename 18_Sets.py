# Set are used to remove duplicates
# they are unordered separation of uniques values
numbers = [1, 2, 3, 1, 2, 3, 5, 5, 6]
first = set(numbers)
second = {1, 2, 3, 0, 9, 8}
print("Union of 2 set numbers", first | second)
print("Intersection of 2 set", first & second)
print("Difference between set of numbers", first - second)
print("Semantic difference set of numbers", first ^ second)