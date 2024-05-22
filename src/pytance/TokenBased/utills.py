def bag_distance(set1, set2):
    # Check if both inputs are sets
    if not isinstance(set1, set) or not isinstance(set2, set):
        raise TypeError("Both inputs must be sets.")
        
    symmetric_difference_size = len(set1.symmetric_difference(set2))
    return symmetric_difference_size


def dice_coefficient(set1, set2):
    # Check if both inputs are sets
    if not isinstance(set1, set) or not isinstance(set2, set):
        raise TypeError("Both inputs must be sets.")
        
    intersection_size = len(set1.intersection(set2))
    sum_size = len(set1) + len(set2)
    return 2 * intersection_size / float(sum_size)

def jaccard_similarity(set1, set2):
    # Check if both inputs are sets
    if not isinstance(set1, set) or not isinstance(set2, set):
        raise TypeError("Both inputs must be sets.")
        
    intersection_size = len(set1.intersection(set2))
    union_size = len(set1.union(set2))
    return intersection_size / float(union_size)

def overlap_coefficient(set1, set2):
    # Check if both inputs are sets
    if not isinstance(set1, set) or not isinstance(set2, set):
        raise TypeError("Both inputs must be sets.")
        
    intersection_size = len(set1.intersection(set2))
    min_size = min(len(set1), len(set2))
    return intersection_size / float(min_size)

def qgram_similarity(str1, str2, q):
    # Check if both inputs are sets
    if not isinstance(set1, set) or not isinstance(set2, set):
        raise TypeError("Both inputs must be sets.")
        
    set1 = set([str1[i:i+q] for i in range(len(str1)-q+1)])
    set2 = set([str2[i:i+q] for i in range(len(str2)-q+1)])
    common_qgrams = set1.intersection(set2)
    return len(common_qgrams) / float(max(len(set1), len(set2)))