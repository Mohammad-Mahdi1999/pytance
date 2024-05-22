def longest_common_substring(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    result = 0  # To store the length of the longest common substring
    end_index = 0  # To store the ending index of the longest common substring

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > result:
                    result = dp[i][j]
                    end_index = i - 1
            else:
                dp[i][j] = 0

    return X[end_index - result + 1:end_index + 1]

# Example usage:
X = "ABCBDAB"
Y = "BDCAB"
result = longest_common_substring(X, Y)
print("Longest Common Substring:", result)


