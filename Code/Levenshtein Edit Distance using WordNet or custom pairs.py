def levenshtein_distance(a, b):
    dp = [[0] * (len(b)+1) for _ in range(len(a)+1)]

    for i in range(len(a)+1):
        for j in range(len(b)+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],    # remove
                                   dp[i][j-1],    # insert
                                   dp[i-1][j-1])  # replace
    return dp[len(a)][len(b)]

if __name__ == "__main__":
    pairs = [("kitten", "sitting"), ("flaw", "lawn"), ("intention", "execution")]
    for a, b in pairs:
        dist = levenshtein_distance(a, b)
        print(f"Distance between '{a}' and '{b}' is {dist}")
