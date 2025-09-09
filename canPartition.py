from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        转换下思路：
        1. 这个数组的和必然为偶数， 如果为奇数无法拆分。

        如果为偶数
        2. 这个问题就变成， 能否找到一个子数组， 其和为整个数组的和的一半。
        变成背包问题:

        dp[i] 为能否构成总数量为i的子数组。
        dp[i] = dp[i] or dp[i-k] for k in target ... num
        边界条件:
        dp[0] = True
        dp[i] = False # 初始化条件
        """
        summation = sum(nums)
        if summation % 2:
            return False

        target = summation // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[target]
