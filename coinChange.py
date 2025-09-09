from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """

        假设:
        dp[i] 代表对于 i 数量的最少个数， 那么:

        dp[i] = min(dp[i-k] + 1) for k in coins.

        边界条件:
        dp[0] = 0
        dp[k] = 1 for k in coins.
        注意下边界条件， 和k和i的溢出

        """

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for k in coins:
            if k <= amount:
                # 更大的用不到了
                dp[k] = 1
        coins = set(coins)

        for i in range(1, amount + 1):
            for k in coins:
                if k <= i:  # 防止越界
                    dp[i] = min(dp[i - k] + 1, dp[i])

        return dp[-1] if dp[-1] != amount + 1 else -1
