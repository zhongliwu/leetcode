# -*- coding: utf-8 -*-

import pytest
from bfs import t761_smallest_subset as question


class TestT761SmallestSubset:

    @pytest.fixture
    def solution(self):
        return question.min_elements

    def test_official_sample(self, solution):
        assert solution([3, 1, 7, 1]) == 1

    def test_official_sample_ii(self, solution):
        assert solution([2, 1, 2]) == 2
