from typing import List, Optional


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """

        思路:
        1. 从右往左找到第一个上升的节点。 找到这个i
        2. 从右往左找， 找到正好小于i的j。 如果找到了，那么交换排序。
        3. 反转i到j的位置。
        """
        n = len(nums)
        i = n - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 找到j
        if i >= 0:
            j = n - 1
            while j > i and nums[i] >= nums[j]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        else:
            pass
            # -1
            # 不用调整了。

        # 3. 反转

        left = i + 1
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
