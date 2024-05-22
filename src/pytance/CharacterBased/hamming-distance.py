from __future__ import annotations

def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Hamming distance is defined only for strings of equal length.")
    
    distance = 0
    
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            distance += 1
    
    return distance
'''

# Example Usage
word1 = "coding"
word2 = "coffee"

try:
    distance = hamming_distance(word1, word2)
    print(f"The Hamming distance between '{word1}' and '{word2}' is: {distance}")
except ValueError as e:
    print(f"Error: {e}")
'''
