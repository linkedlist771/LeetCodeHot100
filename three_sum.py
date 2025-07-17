from collections import defaultdict
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """

        使用双指针来解决这个问题， 首先把数组排序， 然后遍历每个元素来找到其对应的和。
        找到后就由于数组的有序性，可以过滤掉相同的元素， 并且由于数组的有序性， 可以对应的移动left和right的位置。

        """

        nums = sorted(nums)
        size = len(nums)
        ans = []

        for i in range(size - 2):
            # 跳过重复的i， 并且这个是从后面往前面条过程
            if nums[i] == nums[i - 1] and i != 0:  # 0 号元素不能跳过, 不然python里面就是和最后一个在比较了
                continue
            # 留下位置个left 和right指正
            left = i + 1
            right = size - 1
            target = -nums[i]

            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    # 找到了， 添加这个，然后进行继续
                    ans.append([nums[i], nums[left], nums[right]])
                    # 剔除掉相同的元素
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # 移动到下一个元素
                    left += 1
                    right -= 1
                elif current_sum > target:
                    # 比这个大那么right左移动
                    right -= 1
                else:
                    left += 1

        return ans
