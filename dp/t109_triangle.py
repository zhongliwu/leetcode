# -*- coding: utf-8 -*-

from typing import (
    List,
)


# top-down approach
def minimum_total(triangle: List[List[int]]) -> int:
    # write your code here
    if triangle is None or len(triangle) == 0 or len(triangle[0]) == 0:
        return 0

    n = len(triangle)
    dp = [[0] * (i + 1) for i in range(n)]

    dp[0][0] = triangle[0][0]
    for i in range(1, n):
        dp[i][0] = triangle[i][0] + dp[i - 1][0]
        dp[i][i] = triangle[i][i] + dp[i - 1][i - 1]

    for i in range(2, n):
        for j in range(1, i):
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]

    return min(dp[n - 1])


