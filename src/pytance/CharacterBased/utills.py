def hamming_distance(str1, str2):
    """
    Calculate the Hamming distance between two strings.
    The Hamming distance is the number of positions at which the corresponding symbols are different.

    Parameters:
    str1 (str): The first input string.
    str2 (str): The second input string.

    Returns:
    int: The Hamming distance between str1 and str2.
    
    Raises:
    TypeError: If either input is not a string.
    ValueError: If the lengths of the strings are not equal.
    """
    # Ensure both inputs are strings
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both inputs must be strings.")
    
    # Hamming distance is only defined for strings of equal length
    if len(str1) != len(str2):
        raise ValueError("Hamming distance is defined only for strings of equal length.")
    
    # Initialize distance counter
    distance = 0
    
    # Compare each character and increment distance for each mismatch
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            distance += 1
    
    return distance

def damerau_levenshtein_distance(str1, str2):
    """
    Calculate the Damerau-Levenshtein distance between two strings.
    This distance is the number of operations (insertions, deletions, substitutions, or transpositions of two adjacent characters) required to change one string into the other.

    Parameters:
    str1 (str): The first input string.
    str2 (str): The second input string.

    Returns:
    int: The Damerau-Levenshtein distance between str1 and str2.
    
    Raises:
    TypeError: If either input is not a string.
    """
    # Ensure both inputs are strings
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both inputs must be strings.")
        
    # Initialize matrix dimensions
    m, n = len(str1), len(str2)
    
    # Create a matrix to store distances
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Populate the matrix with distances
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j  # Deletion cost
            elif j == 0:
                dp[i][j] = i  # Insertion cost
            else:
                # Calculate cost based on previous operations and check for transposition
                dp[i][j] = min(
                    dp[i - 1][j] + 1,  # Deletion
                    dp[i][j - 1] + 1,  # Insertion
                    dp[i - 1][j - 1] + (0 if str1[i - 1] == str2[j - 1] else 1)  # Substitution
                )
                # Check for transposition
                if i > 1 and j > 1 and str1[i - 1] == str2[j - 2] and str1[i - 2] == str2[j - 1]:
                    dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + 1)

    return dp[m][n]

def jaro_distance(str1, str2):
    """
    Calculate the Jaro distance between two strings.
    The Jaro distance is a measure of similarity between two strings and is a float between 0 and 1.
    A value of 1 means an exact match and 0 means there is no similarity.

    Parameters:
    str1 (str): The first input string.
    str2 (str): The second input string.

    Returns:
    float: The Jaro distance between str1 and str2.
    
    Raises:
    TypeError: If either input is not a string.
    """
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
    """
    Calculate the Levenshtein distance between two strings.
    The Levenshtein distance is a measure of the number of single-character edits required to change one word into the other.

    Parameters:
    str1 (str): The first input string.
    str2 (str): The second input string.

    Returns:
    int: The Levenshtein distance between str1 and str2.
    
    Raises:
    TypeError: If either input is not a string.
    """
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
                dp[i][j] = j  # Cost of deletions
            elif j == 0:
                dp[i][j] = i  # Cost of insertions
            else:
                # Calculate cost based on previous operations
                dp[i][j] = min(
                    dp[i - 1][j] + 1,  # Deletion
                    dp[i][j - 1] + 1,  # Insertion
                    dp[i - 1][j - 1] + (0 if str1[i - 1] == str2[j - 1] else 1)  # Substitution
                )

    # Return the Levenshtein distance
    return dp[m][n]

def jaro_winkler_distance(str1, str2, p=0.1):
    """
    Calculate the Jaro-Winkler distance between two strings.
    
    The Jaro-Winkler distance is a measure of similarity between two strings.
    It is a variant of the Jaro distance metric but includes an adjustment
    for common prefixes.

    Parameters:
    str1 (str): First input string.
    str2 (str): Second input string.
    p (float): Scaling factor for common prefix length (default is 0.1).

    Returns:
    float: The Jaro-Winkler distance between str1 and str2.
    """

    # Check if both inputs are strings
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both inputs must be strings.")
    
    # Calculate the Jaro distance using a helper function
    jaro_dist = jaro_distance(str1, str2)  # Assume jaro_distance is defined elsewhere

    # Calculate the common prefix length up to a maximum of 4 characters
    common_prefix_len = 0
    for char1, char2 in zip(str1, str2):
        if char1 == char2 and common_prefix_len < 4:
            common_prefix_len += 1
        else:
            break

    # Apply the Jaro-Winkler adjustment
    # The adjustment is the product of the scaling factor 'p' and the common prefix length
    # This product is then multiplied by the difference of 1 and the Jaro distance
    jaro_winkler_dist = jaro_dist + p * common_prefix_len * (1 - jaro_dist)

    return jaro_winkler_dist