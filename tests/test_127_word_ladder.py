# -*- coding: utf-8 -*-

import pytest
from bfs import _127_word_ladder as question


class Test127WordLadder:

    @pytest.fixture
    def solution(self):
        return question.ladderLength

    def test_official_sample(self, solution):
        start = "leet"
        end = "code"
        word_list = ["lest", "leet", "lose", "code", "lode", "robe", "lost"]
        solution(start, end, word_list)
