# -*- coding: utf-8 -*-

import pytest
from binarysearch import t140_fast_power as question


class TestT140FastPower:

    @pytest.fixture
    def solution(self):
        return question.fast_power

    def test_official_sample(self, solution):
        assert solution(3, 7, 5) == 5
