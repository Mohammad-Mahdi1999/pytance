def dice_coefficient(set1, set2):
    intersection_size = len(set1.intersection(set2))
    sum_size = len(set1) + len(set2)
    return 2 * intersection_size / float(sum_size)

# Example usage:
set1 = set(["apple", "orange", "banana"])
set2 = set(["banana", "kiwi", "orange"])
result = dice_coefficient(set1, set2)
print("Dice Coefficient:", result)


