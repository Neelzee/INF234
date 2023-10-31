INSERT = 1
DELETE = 2
WRONG = 1


INSERT = 1
DELETE = 2
WRONG = 1


def levenshtein_distance(str1, str2):
    m, n = len(str1), len(str2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i][j - 1] + INSERT,    # Insert
                    dp[i - 1][j] + DELETE,    # Delete
                    dp[i - 1][j - 1] + WRONG  # Replace
                )

    return dp[m][n]


print(
    f"Levenshtein distance: {levenshtein_distance('INTENTION', 'EXECUTION')}"
)
print(f"Levenshtein distance: {levenshtein_distance('MASS', 'PASS')}")
print(f"Levenshtein distance: {levenshtein_distance('PASS', 'PASS')}")
print(f"Levenshtein distance: {levenshtein_distance('NILS', 'MICHAEL')}")
print(f"Levenshtein distance: {levenshtein_distance('PASS', 'PAS')}")
print(f"Levenshtein distance: {levenshtein_distance('PASS', 'PASSS')}")
