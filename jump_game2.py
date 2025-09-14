from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        思路：
        每次记录当前可以调到的最远的距离，
        然后每次跳转后， 每次记录最远可跳距离。
        """
        fast_pos = 0
        current_end = 0
        n = len(nums)
        if n <= 1:
            return 0
        jump = 0
        for idx, num in enumerate(nums):
            fast_pos = max(fast_pos, idx + num)

            if idx == current_end:
                current_end = fast_pos
                jump += 1
                if current_end >= n - 1:
                    break
        return jump
