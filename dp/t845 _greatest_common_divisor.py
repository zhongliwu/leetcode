# -*- coding: utf-8 -*-

def gcd(a, b):
    # write your code here
    if a == 0 or b == 0:
        return 0

    small = min(abs(a), abs(b))
    big = max(abs(a), abs(b))
    while big % small != 0:
        small, big = big % small, small

    return small
