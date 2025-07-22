from itertools import product
from typing import List

# from functools import


# cycle
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        思路，先求整个的积， 然后对于每个进行除 => pass， 要求不使用除法。

        对于每个元素， 其除自身外的乘积就是左边的乘以右边的。
        """

        n = len(nums)

        ans = [1] * n

        # 先求左边的乘积
        left = 1
        for i in range(n):
            ans[i] *= left

            left *= nums[i]

        # 然后乘以右边的。

        right = 1

        for i in range(n - 1, -1, -1):
            ans[i] *= right
            right *= nums[i]
        return ans
