# -*- coding: utf-8 -*-

import collections


def k_distinct_characters(s: str, k: int) -> int:
    # Write your code here
    if not s:
        return 0

    n, ans, j = len(s), 0, 0
    distincts = collections.defaultdict(int)
    for i in range(0, n):
        while j < n and len(distincts) < k:
            distincts[s[j]] += 1
            j += 1

        if j < n:
            ans += (n - j + 1)
        elif len(distincts) >= k:
            ans += 1

        distincts[s[i]] -= 1
        if distincts[s[i]] <= 0:
            del distincts[s[i]]

    return ans
