# -*- coding: utf-8 -*-

import pytest
from twopointers import t600_smallest_rectangle_enclosing_black_pixels as question


class Test300LengthOfLIS:

    @pytest.fixture
    def solution(self):
        return question.min_area

    def test_official_sample(self, solution):
        image = ["0010", "0110", "0100"]
        assert solution(image, 0, 2) == 6
