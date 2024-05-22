def gestalt_pattern_matching(pattern, text):
    # str2our gestalt pattern matching logic here
    # This could involve comparing patterns based on structure, not just characters
    # This example simply checks if the pattern is a substring of the text
    if pattern in text:
        return True
    else:
        return False


def longest_common_subsequence(str1, str2):
    # Check if both inputs are strings
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both inputs must be strings.")
        
    m, n = len(str1), len(str2)
    # Create a table to store lengths of LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Building the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstructing the LCS
    lcs_seq = []
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs_seq.insert(0, str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(lcs_seq)

def longest_common_substring(str1, str2):
    
    # Check if both inputs are strings
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both inputs must be strings.")
        
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    result = 0  # To store the length of the longest common substring
    end_index = 0  # To store the ending index of the longest common substring

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > result:
                    result = dp[i][j]
                    end_index = i - 1
            else:
                dp[i][j] = 0

    return str1[end_index - result + 1:end_index + 1]