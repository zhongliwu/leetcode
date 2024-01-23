# -*- coding: utf-8 -*-


import pytest
from twopointers import _424_longest_repeating_character_replacement as question


class Test424LongestRepeatingCharacterReplacement:

    @pytest.fixture
    def bf_solution(self):
        return question.brute_force

    def test_official_sample(self, bf_solution):
        assert bf_solution('ABAB', 2) == 4
