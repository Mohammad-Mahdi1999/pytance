from __future__ import annotations

def jaro_distance(str1, str2):
    # Calculate the length of the strings
    len_str1, len_str2 = len(str1), len(str2)

    # Set the matching distance (up to which characters are considered matching)
    match_distance = max(len_str1, len_str2) // 2 - 1

    # Initialize arrays to store matching characters
    matches_str1, matches_str2 = [False] * len_str1, [False] * len_str2

    # Count the number of matching characters
    match_count = 0
    for i in range(len_str1):
        start = max(0, i - match_distance)
        end = min(i + match_distance + 1, len_str2)
        for j in range(start, end):
            if not matches_str2[j] and str1[i] == str2[j]:
                matches_str1[i], matches_str2[j] = True, True
                match_count += 1
                break

    if match_count == 0:
        return 0.0

    # Count the number of transpositions
    transpositions = 0
    k = 0
    for i in range(len_str1):
        if matches_str1[i]:
            while not matches_str2[k]:
                k += 1
            if str1[i] != str2[k]:
                transpositions += 1
            k += 1

    transpositions //= 2  # Count each transposition only once

    # Calculate the Jaro distance
    jaro_similarity = (match_count / len_str1 + match_count / len_str2 + (match_count - transpositions) / match_count) / 3
    return jaro_similarity
'''
# Example Usage
word1 = "coding"
word2 = "coffee"
distance = jaro_distance(word1, word2)
print(f"The Jaro distance between '{word1}' and '{word2}' is: {distance:.4f}")

'''
