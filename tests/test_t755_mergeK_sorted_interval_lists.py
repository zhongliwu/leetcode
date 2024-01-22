# -*- coding: utf-8 -*-

import pytest
from datasturcture import t755_mergeK_sorted_interval_lists as question
from utils.Graph import Interval
from utils import ArrayUtils


class TestT755MergeKSortedIntervalLists:

    @pytest.fixture
    def solution(self):
        return question.merge_k_sorted_interval_lists

    def test_official_sample(self, solution):
        intervals = [
            [Interval(1, 3), Interval(4, 7), Interval(6, 8)],
            [Interval(1, 2), Interval(9, 10)]
        ]
        merged = solution(intervals)
        expected = [
            Interval(1, 3), Interval(4, 8), Interval(9, 10)
        ]
        assert ArrayUtils.compare_interval_lists(merged, expected) is True

    def test_one_interval(self, solution):
        intervals = [
            [Interval(1, 5)]
        ]
        merged = solution(intervals)
        expected = [Interval(1, 5)]
        assert ArrayUtils.compare_interval_lists(merged, expected)

    def test_two_intervals_in_a_row(self, solution):
        intervals = [
            [Interval(1, 3), Interval(2, 7)]
        ]
        merged = solution(intervals)
        expected = [Interval(1, 7)]
        assert ArrayUtils.compare_interval_lists(merged, expected)

    def test_two_interval_in_two_rows(self, solution):
        intervals = [
            [Interval(1, 7)],
            [Interval(8, 10)]
        ]
        merged = solution(intervals)
        expected = [Interval(1, 7), Interval(8, 10)]
        assert ArrayUtils.compare_interval_lists(merged, expected)

    def test_three_interval_lists_and_one_empty_list(self, solution):
        intervals = [
            [Interval(1, 2)],
            [Interval(1, 5), Interval(6, 7)],
            [],
            [Interval(7, 10), Interval(11, 19), Interval(21, 22)]
        ]
        merged = solution(intervals)
        expected = [Interval(1, 5), Interval(6, 10), Interval(11, 19), Interval(21, 22)]
        assert ArrayUtils.compare_interval_lists(merged, expected)





