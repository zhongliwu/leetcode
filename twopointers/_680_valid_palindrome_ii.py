# -*- coding: utf-8 -*-


def _680_valid_palindrome_ii(s: str) -> bool:
    # Write your code here
    start, end = check_palindrome(s, 0, len(s) - 1)
    if start >= end:
        return True

    return is_palindrome(s, start + 1, end) or is_palindrome(s, start, end - 1)


def check_palindrome(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return start, end

        start += 1
        end -= 1

    return start, end


def is_palindrome(s, start, end):
    left, right = check_palindrome(s, start, end)
    return left >= right
