# -*- coding: utf-8 -*--

import pytest
import _33_search_in_rotated_sorted_array as question


class Test33SearchInRotatedSortedArray:

    @pytest.fixture
    def solution(self):
        return question._33_search_in_rotated_sorted_array

    def test_normal_array(self, solution):
        a = [1, 4, 6, 10, 21]
        result = solution(a, 21)
        expected = 4
        assert result == expected

    def test_pivot_in_right_and_target_in_left(self, solution):
        a = [7, 8, 9, 10, 1, 2]
        result = solution(a, 8)
        assert result == 1

    def test_pivot_in_right_and_target_in_right(self, solution):
        a = [7, 8, 9, 10, 1, 2, 3]
        result = solution(a, 2)
        assert result == 5

    def test_pivot_in_left_and_target_in_left(self, solution):
        a = [7, 1, 2, 3, 6]
        assert solution(a, 1) == 1

    def test_pivot_in_left_and_target_in_right(self, solution):
        a = [10, 1, 2, 3, 5, 7, 8, 9]
        assert solution(a, 7) == 5

    def test_one_boundary(self, solution):
        a = [1]
        assert solution(a, 1) == 0

    def test_two_boundary(self, solution):
        a = [9, 0]
        assert solution(a, 0) == 1
