items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

prices = list(map(lambda item: item[1], items))
print("Actual price", prices)

# The code sample below produce the same output as line 7 and list Comprehension
prices2 = [item[1] for item in items]
print("comprehension list price", prices2)

filtered = list(filter(lambda item: item[1] >= 10, items))
print("Filtered price", filtered)

# The code sample below produce the same output as line 14 and list Comprehension
filtered2 = [item for item in items if item[1] >= 10]
print("Comprehension list price", filtered2)