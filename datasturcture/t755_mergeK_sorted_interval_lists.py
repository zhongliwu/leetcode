# -*- coding: utf-8 -*-

import heapq
from utils.Graph import Interval


def merge_k_sorted_interval_lists(intervals):
    # write your code here
    if not intervals:
        return []

    result, priority_queue, n = [], [], len(intervals)
    heapq.heapify(priority_queue)
    for i in range(0, n):
        if not intervals[i]:
            continue
        heapq.heappush(priority_queue, ((intervals[i][0].start,
                                         intervals[i][0].end),
                                        i,
                                        0))

    tmp_int, itr_row, itr_col = heapq.heappop(priority_queue)
    push_next_interval(priority_queue, intervals, itr_row, itr_col)
    while len(priority_queue) > 0:
        cur_int, itr_row, itr_col = heapq.heappop(priority_queue)
        if tmp_int[1] >= cur_int[0]:
            tmp_int = (tmp_int[0], max(tmp_int[1], cur_int[1]))
        else:
            elem = Interval(tmp_int[0], tmp_int[1])
            result.append(elem)
            tmp_int = cur_int

        push_next_interval(priority_queue, intervals, itr_row, itr_col)

    last = Interval(tmp_int[0], tmp_int[1])
    result.append(last)
    return result


def push_next_interval(priority_queue, intervals, cur_row, cur_col):
    cur_col += 1
    if cur_col < len(intervals[cur_row]):
        heapq.heappush(priority_queue,
                       ((intervals[cur_row][cur_col].start,
                         intervals[cur_row][cur_col].end),
                        cur_row,
                        cur_col))
