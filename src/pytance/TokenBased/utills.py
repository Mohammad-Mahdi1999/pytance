def bag_distance(set1, set2):
    """
    Calculate the bag distance (symmetric difference) between two sets.

    Parameters:
    set1 (set): The first input set.
    set2 (set): The second input set.

    Returns:
    int: The size of the symmetric difference between set1 and set2.
    """
    # Check if both inputs are sets
    if not isinstance(set1, set) or not isinstance(set2, set):
        raise TypeError("Both inputs must be sets.")
        
    symmetric_difference_size = len(set1.symmetric_difference(set2))
    return symmetric_difference_size

def dice_coefficient(set1, set2):
    """
    Calculate the Dice coefficient between two sets.

    Parameters:
    set1 (set): The first input set.
    set2 (set): The second input set.

    Returns:
    float: The Dice coefficient value (ranging from 0 to 1).
    """
    # Check if both inputs are sets
    if not isinstance(set1, set) or not isinstance(set2, set):
        raise TypeError("Both inputs must be sets.")
        
    intersection_size = len(set1.intersection(set2))
    sum_size = len(set1) + len(set2)
    return 2 * intersection_size / float(sum_size)

def jaccard_similarity(set1, set2):
    """
    Calculate the Jaccard similarity between two sets.

    Parameters:
    set1 (set): The first input set.
    set2 (set): The second input set.

    Returns:
    float: The Jaccard similarity value (ranging from 0 to 1).
    """
    # Check if both inputs are sets
    if not isinstance(set1, set) or not isinstance(set2, set):
        raise TypeError("Both inputs must be sets.")
        
    intersection_size = len(set1.intersection(set2))
    union_size = len(set1.union(set2))
    return intersection_size / float(union_size)

def overlap_coefficient(set1, set2):
    """
    Calculate the overlap coefficient between two sets.

    Parameters:
    set1 (set): The first input set.
    set2 (set): The second input set.

    Returns:
    float: The overlap coefficient value (ranging from 0 to 1).
    """
    # Check if both inputs are sets
    if not isinstance(set1, set) or not isinstance(set2, set):
        raise TypeError("Both inputs must be sets.")
        
    intersection_size = len(set1.intersection(set2))
    min_size = min(len(set1), len(set2))
    return intersection_size / float(min_size)

def qgram_similarity(str1, str2, q):
    """
    Calculate the q-gram similarity between two strings.

    Parameters:
    str1 (str): The first input string.
    str2 (str): The second input string.
    q (int): The q-gram size.

    Returns:
    float: The q-gram similarity value (ranging from 0 to 1).
    """
    # Check if both inputs are strings
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both inputs must be strings.")
        
    set1 = set([str1[i:i+q] for i in range(len(str1)-q+1)])
    set2 = set([str2[i:i+q] for i in range(len(str2)-q+1)])
    common_qgrams = set1.intersection(set2)
    return len(common_qgrams) / float(max(len(set1), len(set2)))
