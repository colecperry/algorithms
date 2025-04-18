def longest_common_subsequence(text1: str, text2: str) -> str:
    m, n = len(text1), len(text2)
    
    # Create a 2D dp array initialized with 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill dp array
    for i in range(m):
        for j in range(n):
            if text1[i] == text2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

    # Reconstruct the LCS from dp table
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i-1] == text2[j-1]:
            lcs.append(text1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs))