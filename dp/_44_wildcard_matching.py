# -*- coding: utf-8 -*-


def is_match(s: str, p: str) -> bool:
    # write your code here
    if not s or not p:
        return False

    n, m = len(s), len(p)
    dp = [
        [False] * (m + 1) for _ in range(n + 1)
    ]

    dp[0][0] = True
    for j in range(1, m + 1):
        dp[0][j] = dp[0][j - 1] and (p[j - 1] == '*')

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if p[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] and matches(s[i - 1], p[j - 1])

    return dp[n][m]


def matches(c: str, p: str) -> bool:
    return c == p or p == '?'
