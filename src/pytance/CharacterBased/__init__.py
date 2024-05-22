
from __future__ import annotations

from .utills import hamming_distance, damerau_levenshtein_distance, jaro_distance, levenshtein_distance,jaro_winkler_distance
# from . import utills

__all__ = ["hamming_distance", "damerau_levenshtein_distance", "jaro_distance", "levenshtein_distance", "jaro_winkler_distance"]

functions = {
          "hamming": hamming_distance,
          "damerau_levenshtein": damerau_levenshtein_distance,
          "jaro": jaro_distance,
          "levenshtein": levenshtein_distance,
          "jaro_winkler": jaro_winkler_distance
        }

def dist(word1, word2, function_name = 'hamming'):
    if function_name in functions:
        return functions[function_name](word1, word2)
    else:
        raise ValueError(f"No such function: {function_name} in CharacterBased")