# -*- coding: utf-8 -*-

import pytest
from divideandconquer import t5_kth_largest_element as question


class TestT5KthLargestElement:

    @pytest.fixture
    def solution(self):
        return question.kth_largest_element

    def test_official_sample(self, solution):
        assert solution(1, [1, 3, 4, 2]) == 4

    def test_one_number(self, solution):
        assert solution(1, [3]) == 3

    def test_two_number(self, solution):
        assert solution(2, [8, 1]) == 1

    # -3 1 1 2 5 6 7 8 9 10 11 21
    def test_array_more_than_10_number(self, solution):
        assert solution(3, [10, 21, 1, -3, 7, 11, 9, 8, 1, 2, 6, 5]) == 10
