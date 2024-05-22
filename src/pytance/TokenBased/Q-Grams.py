def qgram_similarity(str1, str2, q):
    set1 = set([str1[i:i+q] for i in range(len(str1)-q+1)])
    set2 = set([str2[i:i+q] for i in range(len(str2)-q+1)])
    common_qgrams = set1.intersection(set2)
    return len(common_qgrams) / float(max(len(set1), len(set2)))

# Example usage:
str1 = "apple"
str2 = "apricot"
q = 2
result = qgram_similarity(str1, str2, q)
print(f"Q-Gram Similarity (q={q}): {result}")


