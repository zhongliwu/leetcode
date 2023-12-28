# -*- coding: utf-8 -*-

import pytest
from dfs import t16_permutations_ii as question
from utils.ArrayUtils import compare_compound_lists as comparator


class TestT16PermutationsII:

    @pytest.fixture
    def solution(self):
        return question.permute_unique

    def test_sample(self, solution):
        nums = [1, 1]
        assert comparator(solution(nums), [[1, 1]])

    def test_multiple_duplicate(self, solution):
        nums = [1, 1, 2, 2, 2]
        expected = [
            [1, 1, 2, 2, 2],
            [1, 2, 1, 2, 2],
            [1, 2, 2, 1, 2],
            [1, 2, 2, 2, 1],
            [2, 1, 1, 2, 2],
            [2, 1, 2, 1, 2],
            [2, 1, 2, 2, 1],
            [2, 2, 1, 1, 2],
            [2, 2, 1, 2, 1],
            [2, 2, 2, 1, 1]
        ]
        assert comparator(solution(nums), expected)
