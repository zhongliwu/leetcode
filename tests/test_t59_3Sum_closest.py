# -*- coding: utf-8 -*-

import pytest
from twopointers import t59_3Sum_closest as question


class TestT593SumClosest:

    @pytest.fixture
    def solution(self):
        return question.three_sum_closest

    def test_official_sample(self, solution):
        assert solution([2, 7, 11, 15], 3) == 20
