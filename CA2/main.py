INSERT = 1
DELETE = 2
WRONG = 1


def levenshtein_distance(word1, word2):
    m, n = len(word1), len(word2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    return dp[m][n]

print(f"Levenshtein distance: {levenshtein_distance('INTENTION', 'EXECUTION')}")
print(f"Levenshtein distance: {levenshtein_distance('MASS', 'PASS')}")
print(f"Levenshtein distance: {levenshtein_distance('PASS', 'PASS')}")
print(f"Levenshtein distance: {levenshtein_distance('PASS', 'PASS')}")
print(f"Levenshtein distance: {levenshtein_distance('NILS', 'MICHAEL')}")
