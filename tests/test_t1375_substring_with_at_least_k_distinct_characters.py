# -*- coding: utf-8 -*-

import pytest
from twopointers import t1375_substring_with_at_least_k_distinct_characters as question


class TestT1375SubstringWithAtLeastKDistinctCharacters:

    @pytest.fixture
    def solution(self):
        return question.k_distinct_characters

    def test_official_sample(self, solution):
        assert solution('abcabcabca', 4) == 0

    def test_official_sample_ii(self, solution):
        assert solution('abcabcabcabc', 3) == 55

    def test_only_one_substr(self, solution):
        assert solution('aaaaaaaaaabbbbbc', 3) == 10

    def test_duplicate_char(self, solution):
        assert solution('abccccccccccc', 3) == 11

    def test_one_substr(self, solution):
        assert solution('abc', 1) == 6

    def test_multiple_duplicates(self, solution):
        assert solution('abacabcaac', 3) == 31

