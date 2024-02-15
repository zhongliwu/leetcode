# -*- coding: utf-8 -*-

import pytest
from dp import _44_wildcard_matching as question


class Test44WildcardMatching:

    @pytest.fixture
    def solution(self):
        return question.is_match

    def test_official_sample(self, solution):
        assert solution('a', 'aa') is False

