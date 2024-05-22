def overlap_coefficient(set1, set2):
    intersection_size = len(set1.intersection(set2))
    min_size = min(len(set1), len(set2))
    return intersection_size / float(min_size)

# Example usage:
set1 = set(["apple", "orange", "banana"])
set2 = set(["banana", "kiwi", "orange"])
result = overlap_coefficient(set1, set2)
print("Overlap Coefficient:", result)


