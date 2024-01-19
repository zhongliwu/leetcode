# -*- coding: utf-8 -*-

import pytest
from dp import t109_triangle as question


class TestT109Triangle:

    @pytest.fixture
    def solution(self):
        return question.minimum_total

    def test_official_sample(self, solution):
        triangle = [[-1], [2, 3], [1, -1, -3]]
        assert solution(triangle) == -1
