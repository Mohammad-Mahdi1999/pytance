from __future__ import annotations

def damerau_levenshtein_distance(str1, str2):
    m, n = len(str1), len(str2)
    
    # Initialize a matrix to store costs
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill in the matrix with costs
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,          # Deletion
                    dp[i][j - 1] + 1,          # Insertion
                    dp[i - 1][j - 1] + (0 if str1[i - 1] == str2[j - 1] else 1)  # Substitution
                )
                
                # Check for transposition
                if i > 1 and j > 1 and str1[i - 1] == str2[j - 2] and str1[i - 2] == str2[j - 1]:
                    dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + 1)

    # Return the Damerau-Levenshtein distance
    return dp[m][n]
'''

# Example Usage
word1 = "coding"
word2 = "coffee"
distance = damerau_levenshtein_distance(word1, word2)
print(f"The Damerau-Levenshtein distance between '{word1}' and '{word2}' is: {distance}")'''
