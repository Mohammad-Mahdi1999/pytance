
from .utills import editex, smith_waterman, syllable_alignment
from . import utills

__all__ = ["editex", "smith_waterman", "syllable_alignment"]

def dist(word1, word2, function_name):
    # Dynamically call the function based on the function_name argument
    if hasattr(utills, function_name):
        func = getattr(utills, function_name)
        return func(word1, word2)
    else:
        raise ValueError(f"No such function: {function_name} in PhoneticSensitive")

