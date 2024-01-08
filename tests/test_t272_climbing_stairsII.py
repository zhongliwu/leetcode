# -*- coding: utf-8 -*-

import pytest
from dfs import t272_climbing_stairsII as question


class TestT272ClimbingStairsII:

    @pytest.fixture
    def solution(self):
        return question.climbing_stairs2

    def test_sampler(self, solution):
        assert solution(3) == 4
