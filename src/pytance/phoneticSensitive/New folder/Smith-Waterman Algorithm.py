def smith_waterman(s1, s2, match_score=2, mismatch_penalty=-1, gap_penalty=-1):
    m, n = len(s1), len(s2)
    matrix = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = matrix[i - 1][j - 1] + (match_score if s1[i - 1] == s2[j - 1] else mismatch_penalty)
            delete = matrix[i - 1][j] + gap_penalty
            insert = matrix[i][j - 1] + gap_penalty
            matrix[i][j] = max(0, match, delete, insert)

    # Find the maximum score in the matrix
    max_score = max(max(row) for row in matrix)
    
    # Find the indices of the maximum score
    indices = [(i, j) for i in range(m + 1) for j in range(n + 1) if matrix[i][j] == max_score]

    return max_score, indices

# Example usage:
s1 = "kitten"
s2 = "sitting"
score, indices = smith_waterman(s1, s2)
print("Smith-Waterman Score:", score)
print("Alignment Indices:", indices)
