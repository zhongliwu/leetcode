# -*- coding: utf-8 -*--


class NumArray:
    """
    q303: range sum query with immutable array
    """
    def __init__(self, nums: list[int]):
        self.prefix_arr = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            self.prefix_arr[i] = self.prefix_arr[i - 1] + nums[i - 1]

    def sum_range(self, left: int, right: int):
        if left > right or left >= (len(self.prefix_arr) - 1) or right >= (len(self.prefix_arr) - 1):
            return 0

        return self.prefix_arr[right + 1] - self.prefix_arr[left]


class NumMatrix:
    """
    q304: range sum query in 2-D matrix
    """
    def __init__(self, matrix: list[list[int]]):
        num_of_row = len(matrix) + 1
        num_of_col = len(matrix[0]) + 1
        self.prefix_matrix = [[0] * num_of_col for i in range(num_of_row)]
        for i in range(1, num_of_row):
            for j in range(1, num_of_col):
                self.prefix_matrix[i][j] = self.prefix_matrix[i - 1][j] + \
                                            self.prefix_matrix[i][j - 1] + \
                                            matrix[i - 1][j - 1] - \
                                            self.prefix_matrix[i - 1][j - 1]

    def sum_region(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix_matrix[row2 + 1][col2 + 1] - \
                self.prefix_matrix[row1][col2 + 1] - \
                self.prefix_matrix[row2 + 1][col1] + \
                self.prefix_matrix[row1][col1]
