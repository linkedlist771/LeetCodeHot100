from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        思路， 构建一个dp数组：
        dp[i] 代表以i序列结尾最长递增子序列， 那么有:
        if nums[j] < nums[i]: for all j < i
            dp[i] = max(dp[i], dp[j] + 1）

        边界条件:
        dp[0] = 1
        初始化的时候每个元素都是1
        """
        n = len(nums)

        dp = [1] * (n)  # 每个至少有一个
        dp[0] = 1
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)  # 是返回最大的，而不是最后一个
