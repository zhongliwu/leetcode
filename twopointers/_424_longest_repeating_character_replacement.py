# -*- coding: utf-8 -*-

import collections


def brute_force(s: str, k: int) -> int:
    if not s:
        return 0

    ans, n = 0, len(s)
    for i in range(0, n):
        for j in range(i + 1, n + 1):
            freq_count = collections.defaultdict(int)
            for itr in range(i, j):
                freq_count[s[itr]] += 1
            max_freq = max(freq_count.values())
            if j - i - max_freq + 1 <= k:
                ans = max(ans, j - i + 1)

    return ans
