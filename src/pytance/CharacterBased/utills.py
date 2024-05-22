def hamming_distance(str1, str2):
    
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both inputs must be strings.")
    
    if len(str1) != len(str2):
        raise ValueError("Hamming distance is defined only for strings of equal length.")
    
    distance = 0
    
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            distance += 1
    
    return distance

def damerau_levenshtein_distance(str1, str2):
    
    # Check if both inputs are strings
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both inputs must be strings.")
        
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

def jaro_distance(str1, str2):
    
    # Check if both inputs are strings
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both inputs must be strings.")
        
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

def levenshtein_distance(str1, str2):
    # Check if both inputs are strings
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both inputs must be strings.")
        
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

    # Return the Levenshtein distance
    return dp[m][n]

def jaro_winkler_distance(str1, str2, p=0.1):
    
    # Check if both inputs are strings
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both inputs must be strings.")
        
    jaro_dist = jaro_distance(str1, str2)  # Change variable name to avoid conflict

    # Calculate the common prefix length
    common_prefix_len = 0
    for char1, char2 in zip(str1, str2):
        if char1 == char2:
            common_prefix_len += 1
        else:
            break

    # Calculate the Jaro-Winkler Distance
    jaro_winkler_dist = jaro_dist + p * common_prefix_len * (1 - jaro_dist)
    return jaro_winkler_dist
