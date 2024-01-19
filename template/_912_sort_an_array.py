# -*- coding: utf-8 -*-

from typing import (
    List,
)


def sort_array(nums: List[int], worker) -> List[int]:
    worker.sort(nums)
    return worker.nums


class Sort:
    def __init__(self, nums: List[int]):
        self.nums = nums
        pass

    def sort(self):
        pass


class QuickSort(Sort):
    def __init__(self, nums: List[int]):
        Sort.__init__(self, nums)
        self.nums = nums

    def sort(self):
        if self.nums is None or len(self.nums) == 0:
            return []

        self.quick_sort(0, len(self.nums) - 1)

    def quick_sort(self, start, end):
        if start >= end:
            return

        left, right, pivot = start, end, self.nums[(start + end) // 2]
        while left <= right:
            while self.nums[left] < pivot and left <= right:
                left += 1

            while self.nums[right] > pivot and left <= right:
                right -= 1

            if left <= right:
                self.nums[left], self.nums[right] = self.nums[right], self.nums[left]
                left += 1
                right -= 1

        self.quick_sort(start, right)
        self.quick_sort(left, end)


class MergeSort(Sort):
    def __init__(self, nums: List[int]):
        Sort.__init__(self, nums)
        self.nums = nums

    def sort(self):
        if self.nums is None or len(self.nums) == 0:
            return []

        n = len(self.nums)
        tmp = [0] * n
        self.merge_sort(0, n - 1, tmp)

    def merge_sort(self, start: int, end: int, tmp: List[int]):
        if start >= end:
            return

        mid = (start + end) // 2
        self.merge_sort(start, mid, tmp)
        self.merge_sort(mid + 1, end, tmp)
        self.merge(tmp, start, end)

    def merge(self, tmp: List[int], start: int, end: int):
        mid = (start + end) // 2
        idx, left_start, right_start = start, start, mid + 1
        while left_start <= mid and right_start <= end:
            if self.nums[left_start] <= self.nums[right_start]:
                tmp[idx] = self.nums[left_start]
                left_start += 1
            else:
                tmp[idx] = self.nums[right_start]
                right_start += 1
            idx += 1

        while left_start <= mid:
            tmp[idx] = self.nums[left_start]
            idx += 1
            left_start += 1

        while right_start <= end:
            tmp[idx] = self.nums[right_start]
            idx += 1
            right_start += 1

        for i in range(start, end + 1):
            self.nums[i] = tmp[i]
