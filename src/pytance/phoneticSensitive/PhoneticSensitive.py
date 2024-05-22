from __future__ import annotations



class CharacterBased:
    def __init__(self,str1,str2):
        # Initialize any necessary state
        self.str1 = str1
        self.str2 = str2

        self.functions = {
            "damerau_levenshtein": damerau_levenshtein_distance,
            "hamming": hamming_distance,
            "jaro": jaro_distance,
            "jaro_winkler": jaro_winkler_distance_distance,
            "levenshtein": levenshtein_distance,
        }
        
    def __call__(self, function_name):
        if function_name in self.functions:
            return self.functionsfunction_name
        else:
            raise ValueError(f"Function {function_name} not found in CharacterBased")
            
    def damerau_levenshtein_distance(self):
        return damerau_levenshtein_distance(self.str1,self.str2)

    def hamming_distance(self):
        return hamming_distance(self.str1,self.str2)
    
    def jaro_distance(self):
        return jaro_distance(self.str1,self.str2)
    
    def jaro_winkler_distance_distance(self):
        return jaro_winkler_distance_distance(self.str1,self.str2)
    
    def levenshtein_distance(self):
        return levenshtein_distance(self.str1,self.str2)
    