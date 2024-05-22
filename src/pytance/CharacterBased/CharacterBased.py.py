from __future__ import annotations

from pytance.CharacterBased import (
    damerau_levenshtein_distance,
    hamming_distance,
    jaro_distance,
    jaro_winkler_distance_distance,
    levenshtein_distance,
    
    )

class CharacterBased:
    def __init__(self,str1,str2):
        # Initialize any necessary state
        
        
        self.functions = {
            "damerau_levenshtein_distance": damerau_levenshtein_distance,
            "hamming_distance": hamming_distance,
            "jaro_distance": jaro_distance,
            "jaro_winkler_distance_distance": jaro_winkler_distance_distance,
            "levenshtein_distance": levenshtein_distance,
        }
        
    def __call__(self, function_name):
        if function_name in self.functions:
            return self.functionsfunction_name
        else:
            raise ValueError(f"Function {function_name} not found in Subset1")
            
    def damerau_levenshtein_distance(self):
        return damerau_levenshtein_distance()

    def hamming_distance(self):
        return hamming_distance()
    
    def jaro_distance(self):
        return jaro_distance()
    
    def jaro_winkler_distance_distance(self):
        return jaro_winkler_distance_distance()
    
    def levenshtein_distance(self):
        return levenshtein_distance()
    