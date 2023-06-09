numbers = [3, 51, 2, 8, 6]
# sort in ascending order
numbers.sort()
print("Ascending numbers", numbers)
# sort in descending order
numbers.sort(reverse=True)
print("Descending numbers", numbers)

# Sorting a tuple list of products in a list
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print("List of product items:", items)