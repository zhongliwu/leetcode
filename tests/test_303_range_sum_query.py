# -*- coding: utf-8 -*--

import pytest
from arrays import Prefix as pr


class Test303RangeSumQuery:

    @pytest.fixture
    def solution(self):
        return pr.NumArray

    def test_empty(self, solution):
        s = solution([])
        assert s.sum_range(0, 0) == 0
        pass

    def test_single(self, solution):
        s = solution([1])
        assert s.sum_range(0, 0) == 1

    def test_out_of_index(self, solution):
        s = solution([1, 9])
        assert s.sum_range(2, 3) == 0

    def test_whole_limit(self, solution):
        s = solution([0, 1, 2])
        assert s.sum_range(0, 2) == 3

    def test_right_limit(self, solution):
        s = solution([1, 3, 5])
        assert s.sum_range(2, 2) == 5

    def test_left_limit(self, solution):
        s = solution([0, 7, 10])
        assert s.sum_range(0, 0) == 0