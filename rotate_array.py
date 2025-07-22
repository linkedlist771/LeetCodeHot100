from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        [(n-k)....(k)]  =>  [(k)....(n-k)] 1. 第一次翻转，后面k个去前面了， 但是是反过来的，所以需要二次翻转。
        """

        def reverse(array: List[int], begin: int, end: int):
            while begin < end:
                array[begin], array[end] = array[end], array[begin]
                begin += 1
                end -= 1

        n = len(nums)
        k %= n

        # 1. 翻转整个数组
        reverse(nums, 0, n - 1)

        # 2. 翻转前面k个
        reverse(nums, 0, k - 1)

        # 3. 翻转后n-k个
        reverse(nums, k, n - 1)
