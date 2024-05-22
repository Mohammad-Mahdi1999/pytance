def bag_distance(set1, set2):
    symmetric_difference_size = len(set1.symmetric_difference(set2))
    return symmetric_difference_size

# Example usage:
set1 = set(["apple", "orange", "banana"])
set2 = set(["banana", "kiwi", "orange"])
result = bag_distance(set1, set2)
print("Bag Distance:", result)
