def gestalt_pattern_matching(pattern, text):
    # Your gestalt pattern matching logic here
    # This could involve comparing patterns based on structure, not just characters
    # This example simply checks if the pattern is a substring of the text
    if pattern in text:
        return True
    else:
        return False

# Example usage:
pattern = "ABC"
text = "ABCDEF"
result = gestalt_pattern_matching(pattern, text)
print("Pattern Matched:", result)


