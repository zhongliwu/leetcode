# -*- coding: utf-8 -*-

import pytest
from dfs import t17_subsets as question
from utils.ArrayUtils import compare_compound_lists as comparator


class TestT17Subsets:

    @pytest.fixture
    def solution(self):
        return question.subsets

    def test_sample(self, solution):
        nums = [0]
        assert comparator(solution(nums), [[], [0]])

    def test_two_element(self, solution):
        nums = [1, 2]
        result = solution(nums)
        print(result)

