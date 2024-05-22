def lcs(X, Y):
    m, n = len(X), len(Y)
    # Create a table to store lengths of LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Building the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstructing the LCS
    lcs_seq = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_seq.insert(0, X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(lcs_seq)

# Example usage:
X = "ABCBDAB"
Y = "BDCAB"
result = lcs(X, Y)
print("Longest Common Subsequence:", result)



