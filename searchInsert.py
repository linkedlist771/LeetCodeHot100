from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 二分查找， 更新左右指针位置。

        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:  # 如果两者相等的话也不应该被排除
            mid = (right - left) // 2 + left
            if nums[mid] > target:
                right = mid - 1  # 因为只是在这个数组里面搜索

            elif nums[mid] < target:
                left = mid + 1

            else:
                return mid

        return left
