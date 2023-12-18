# -*- coding: utf-8 -*-

import pytest
from twopointers import _69_sqrt_x as question


class TestT628MaximumSubtree:

    @pytest.fixture
    def solution(self):
        return question._69_sqrt_x

    def test_sample(self, solution):
        assert solution(8) == 2

    def test_full_number(self, solution):
        assert solution(9) == 3

    def test_number_4(self, solution):
        assert solution(4) == 2

    def test_number_100(self, solution):
        assert solution(100) == 10
