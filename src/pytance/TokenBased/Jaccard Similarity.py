def jaccard_similarity(set1, set2):
    intersection_size = len(set1.intersection(set2))
    union_size = len(set1.union(set2))
    return intersection_size / float(union_size)

# Example usage:
set1 = set(["apple", "orange", "banana"])
set2 = set(["banana", "kiwi", "orange"])
result = jaccard_similarity(set1, set2)
print("Jaccard Similarity:", result)

