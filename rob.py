from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        假设偷前n个的最多钱是dp[n]
        那么dp[n]的选择就是， 拿第n个的钱和不拿第n个钱取大。也就是:
        > 也即拿了第n个， 那么第n-1个不能拿，所以是dp[n-2] 加上去
        > 或者是不拿第n个， 就是dp[n-1]
        dp[n] = max( nums[n] + dp[n-2],  dp[n-1])

        边界条件:
        n = 0
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        dp = [nums[0], max(nums[0], nums[1])]
        for i in range(2, n):
            dp.append(max(nums[i] + dp[i - 2], dp[i - 1]))
        return dp[-1]
