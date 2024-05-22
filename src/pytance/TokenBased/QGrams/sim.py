def qgram_similarity(str1, str2, q):
    """
    Calculate the q-gram similarity between two strings.

    Q-gram similarity is a measure of similarity between two strings based on the
    common q-grams they share. A q-gram is a substring of 'q' length that can be
    used to compare textual similarity. This function computes the similarity by
    finding the number of common q-grams between the two input strings and dividing
    it by the maximum number of q-grams present in either string.

    Parameters:
    str1 (str): The first string to compare.
    str2 (str): The second string to compare.
    q (int): The length of the q-gram.

    Returns:
    float: The q-gram similarity ratio between str1 and str2.

    Raises:
    TypeError: If either str1 or str2 is not a string.
    """

    # Ensure both inputs are strings
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both inputs must be strings.")

    # Generate q-grams for the first string
    # This creates a set of all possible q-grams in str1
    set1 = set([str1[i:i+q] for i in range(len(str1)-q+1)])

    # Generate q-grams for the second string
    # This creates a set of all possible q-grams in str2
    set2 = set([str2[i:i+q] for i in range(len(str2)-q+1)])

    # Find the intersection of both q-gram sets
    # This finds all q-grams that are common between str1 and str2
    common_qgrams = set1.intersection(set2)

    # Calculate the similarity ratio
    # The ratio is the number of common q-grams divided by the maximum number of q-grams in either set
    return len(common_qgrams) / float(max(len(set1), len(set2)))
