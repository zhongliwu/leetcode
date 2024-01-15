# -*- coding: utf-8 -*-

import pytest
from dp import _300_length_of_LIS as question


class Test300LengthOfLIS:

    @pytest.fixture
    def solution(self):
        return question.length_of_lis

    def test_two_numbers(self, solution):
        assert solution([-2, -1]) == 2

    def test_official_sample(self, solution):
        assert solution([0, 1, 0, 3, 2, 3]) == 4

    def test_wrong_ans(self, solution):
        assert solution([10, 1, 11, 2, 12, 3, 11]) == 4
