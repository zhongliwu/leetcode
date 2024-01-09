# -*- coding: utf-8 -*-

import pytest
from twopointers import t610_two_diff as question
from utils.ArrayUtils import compare_arr


class TestT610TwoDiff:

    @pytest.fixture
    def solution(self):
        return question.two_sum7

    def test_positive_num(self, solution):
        assert compare_arr(solution([2, 7, 17, 24], 5), [2, 7])

    def test_two_num(self, solution):
        assert compare_arr(solution([2, 2], 0), [2, 2])

    def test_negative_and_positive_num(self, solution):
        assert compare_arr(solution([1, 0, -1, -5, 10], 2), [-1, 1])

    def test_zeros(self, solution):
        assert compare_arr(solution([2, 1, 1, 0], 0), [1, 1])
