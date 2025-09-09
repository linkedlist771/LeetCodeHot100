class Solution:
    def numSquares(self, n: int) -> int:
        """
        假设
        dp[i] 代表构成i的最少完全平方数。那么：
        dp[i] = min(  dp[i-k^2] + 1    k^2 <= n  )


        边界条件:
        dp[0] = 0
        dp[1] = 1
        记得条件式 <= , 并且初始化这个dp数组

        """

        dp = [n + 1] * (n + 1)

        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            for k in range(1, int(i**0.5) + 1):
                if k**2 <= i:
                    dp[i] = min(dp[i - k**2] + 1, dp[i])

        return dp[n]
