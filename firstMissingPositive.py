from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        由于数组的这样的性质， 那么最后的结果一定是1~n 中的一个数字，
        把数组转换成这也的形式。
        [1,2,3....N] 其中i-1位置为i， 就是排序好的，
        然后从左到右遍历，其中不满足这个条件的就是最小的正数。
        """

        n = len(nums)

        for i in range(n):
            # while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            #     # 正确的交换方式
            #     nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for idx, num in enumerate(nums):
            if num != idx + 1:
                return idx + 1

        return n + 1
