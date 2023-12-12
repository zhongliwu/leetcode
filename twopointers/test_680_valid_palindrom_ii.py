# -*- coding: utf-8 -*--

import pytest
import _680_valid_palindrome_ii as question


class Test680ValidPalindromeII:

    @pytest.fixture
    def solution(self):
        return question._680_valid_palindrome_ii

    def test_sample(self, solution):
        assert solution("abca") is True

    def test_empty(self, solution):
        assert solution("") is True

    def test_one_char(self, solution):
        assert solution("a") is True

    def test_two_char(self, solution):
        assert solution("ab") is True

    def test_two_same_char(self, solution):
        assert solution("aa") is True

    def test_multiple_none_palindrome_char(self, solution):
        assert solution("abcea") is False

    def test_multiple_palindrome_char_with_one_char_del(self, solution):
        assert solution("acccbcbcccxa") is True



