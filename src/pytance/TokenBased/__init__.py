
from .utills import bag_distance, dice_coefficient,jaccard_similarity,overlap_coefficient
from . import utills

__all__ = ["bag_distance", "dice_coefficient",'jaccard_similarity','overlap_coefficient']

def sim(set1, set2, function_name='bag_distance'):
    # Dynamically call the function based on the function_name argument
    if hasattr(utills, function_name):
        func = getattr(utills, function_name)
        return func(set1, set2)
    else:
        raise ValueError(f"No such function: {function_name} in TokenBased")
