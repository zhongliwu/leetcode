# -*- coding: utf-8 -*-

import pytest
from bfs import _t1170_friend_circles as question


class TestT1170FriendCircles:

    @pytest.fixture
    def solution(self):
        return question.find_circle_num

    def test_sample(self, solution):
        m = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
        assert solution(m) == 2

    def test_indirect(self, solution):
        m = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
        assert solution(m) == 1

    def test_more_in_direct(self, solution):
        m = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
        assert solution(m) == 1

    def test_three_directs(self, solution):
        m = [[1, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0],
             [0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 1]]
        assert solution(m) == 3

    def test_indirect_and_direct(self, solution):
        m = [[1, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 0, 0],
             [0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 1]]
        assert solution(m) == 3

