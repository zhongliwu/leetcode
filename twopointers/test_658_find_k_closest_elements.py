# -*- coding: utf-8 -*--

import pytest
import _658_find_k_closest_elements as question
from utils import ArrayUtils


class Test658FindKClosestElements:

    @pytest.fixture
    def solution(self):
        return question.q658_find_k_closest_elements

    def test_right_boundary(self, solution):
        a = [1, 4, 6, 10, 20]
        result = solution(a, 21, 4)
        expected = [20, 10, 6, 4]
        assert ArrayUtils.compare_arr(result, expected) is True

    def test_func(self, solution):
        a = [1, 4, 8, 12, 16, 28, 38]
        result = solution(a, 12, 4)
        expected = [12, 8, 16, 4]
        assert ArrayUtils.compare_arr(result, expected) is True
