from typing import List


class OneDMatrix:
    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.matrix = matrix
        self.m = m
        self.n = n
        self.size = m * n

    def __len__(self):
        return self.size

    def __getitem__(self, idx: int):
        row = idx // self.n
        col = idx % self.n
        return self.matrix[row][col]


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 直接把这个二维数组view成一维的然后二分就行了。
        nums = OneDMatrix(matrix)

        def binary_search(nums):
            n = len(nums)
            left = 0
            right = n - 1

            while left <= right:
                mid = (right - left) // 2 + left

                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1

                else:
                    return True

            return False

        return binary_search(nums)
