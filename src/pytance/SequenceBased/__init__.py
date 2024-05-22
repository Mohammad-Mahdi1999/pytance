
from .utills import longest_common_subsequence, longest_common_substring
from . import utills

__all__ = ["longest_common_subsequence", "longest_common_substring"]

def dist(word1, word2, function_name):
    # Dynamically call the function based on the function_name argument
    if hasattr(utills, function_name):
        func = getattr(utills, function_name)
        return func(word1, word2)
    else:
        raise ValueError(f"No such function: {function_name} in SequenceBased")

