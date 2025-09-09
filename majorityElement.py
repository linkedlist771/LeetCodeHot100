from typing import List, Optional


class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     # 就用哈希吧
    #     threshold = n//2
    #     number_counts = {}
    #
    #     for num in nums:
    #         number_counts[num] = number_counts.get(num, 0) + 1
    #
    #     for k, v in number_counts.items():
    #         if v > threshold:
    #             return k
    #

    def majorityElement(self, nums: List[int]) -> int:
        # 投票方法
        candidate = None
        count = 0
        # 第一阶段：找候选者
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate
