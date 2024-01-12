# -*- coding: utf-8 -*-

import pytest
from twopointers import t28_search_a_2D_matrix as question


class TestT28SearchA2DMatrix:

    @pytest.fixture
    def solution(self):
        return question.search_matrix

    def test_2row_3col(self, solution):
        nums = [
            [1, 4, 5],
            [6, 7, 8]
        ]
        assert solution(nums, 6) is True
