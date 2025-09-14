from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 思路就是获取每个元素他的右边的最大值， 然后所有的最大值取大就行了

        n = len(prices)

        profit = [-1] * n
        right_max = prices[-1]

        for i in range(n - 1, -1, -1):
            p = prices[i]
            profit[i] = right_max - p
            right_max = max(right_max, p)

        max_price = max(profit)

        if max_price < 0:
            return 0

        else:
            return max_price
