from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        1. 由于数组中可能包含负数，负数乘以负数会变成正数，所以需要同时跟踪当前位置的最大值和最小值
        2. 对于每个数字，有三种选择：
           - 单独作为一个子数组（重新开始）
           - 与前面的最大乘积相乘
           - 与前面的最小乘积相乘（负数情况下可能变成最大值）
        3. 动态更新最大值和最小值，并记录全局最大乘积
        4. 时间复杂度：O(n)，空间复杂度：O(1)

        """

        if len(nums) == 1:
            return nums[0]

        max_product = nums[0]
        current_max = nums[0]
        current_min = nums[0]
        # max_product =

        for i in range(1, len(nums)):
            num = nums[i]

            temp_max = current_max
            # 由于可能存在负数的情况， 所以负数的case也要考虑。
            current_max = max(num, current_max * num, current_min * num)
            current_min = min(num, temp_max * num, current_min * num)

            max_product = max(max_product, current_max)

        return max_product
