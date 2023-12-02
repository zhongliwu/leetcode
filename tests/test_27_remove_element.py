# -*- coding: utf-8 -*-

import pytest
from arrays import RemoveElement as re
# import sys
# from os.path import dirname, abspath, join


class Test27RemoveElement:
    @pytest.fixture
    def get_solution_class(self):
        return re.RemoveElement()
    
    def test_empty(self, get_solution_class):
        nums = []
        val = 0
        s = get_solution_class
        r_hat = s.q27_remove_element(nums, val)
        assert r_hat == 0
    
    def test_edges(self, get_solution_class):
        nums = [0]
        val = 0
        s = get_solution_class
        r_hat = s.q27_remove_element(nums, val)
        assert r_hat == 0
    
    def test_pre_exempt(self, get_solution_class):
        nums = [1, 1, 2, 2, 3]
        val = 1
        s = get_solution_class
        r_hat = s.q27_remove_element(nums, val)
        assert r_hat == 3
