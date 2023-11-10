"""
The function levenshtein_distance, takes in two words,
and measures how "far" one string is from another, by
taking into account the number of insertions, deletitions and wrong words.

We do this, by using an iterative technique, that uses a nested-list.

First we take the length of both strings, giving us the dimensions of the list.

We then initalize the nested-list, putting 0 everywher.
Then, for the top-most row, and left most column, we put in 1, 2, ...
As the cost of traversing the list.

Then we iterate over the strings, comparing each pair of chars.

If they are equal, no operation is needed.

If they are not equal, we calculate the minimum between inserting, deleting or substituting the char.

We can do this, because we can visualise it as the cost of moving between rows and columns in the list.

The final result will be in the bottom right of the nested list.

Since we are comparing each char, big O notation, is O(n^2), if the strings have the same length, if not, its O(n * m), where n is one string, and m is the other.
"""

INSERT = 1
DELETE = 2
WRONG = 1


def levenshtein_distance(str1: str, str2: str) -> int:
    """Measusres the similiarity between two strings,
    by taking into account the number of insertions, deletitions and wrong words, needed to transform str1 into str2

    Args:
        str1 (str): Starting word
        str2 (str): End word

    Returns:
        int: Cost of transforming str1 to str2
    """
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


