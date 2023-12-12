# -*- coding: utf-8 -*-

import pytest
import _27_remove_element as question


class Test27RemoveElement:
    @pytest.fixture
    def solution(self):
        return question._27_remove_element
    
    def test_empty(self, solution):
        nums = []
        val = 0
        r_hat = solution(nums, val)
        assert r_hat == 0
    
    def test_edges(self, solution):
        nums = [0]
        val = 0
        r_hat = solution(nums, val)
        assert r_hat == 0
    
    def test_pre_exempt(self, solution):
        nums = [1, 1, 2, 2, 3]
        val = 1
        r_hat = solution(nums, val)
        assert r_hat == 3
