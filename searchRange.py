from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        思路， 做两次二分查找， 一次找左边界， 一次找右边界
        """
        if not nums:
            return [-1, -1]
        n = len(nums)

        # 找左边界
        left_bound = -1

        left = 0
        right = n - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] >= target:
                # 注意这里是大于等于
                right = mid - 1
            else:
                left = mid + 1
        if left < n and target == nums[left]:
            left_bound = left
        else:
            return [-1, -1]

        # 找右边界
        right_bound = -1

        left = 0
        right = n - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] > target:
                # 注意这里是大于等于
                right = mid - 1
            elif nums[mid] == target:
                left = mid + 1
            else:
                left = mid + 1
        if right >= 0 and target == nums[right]:
            right_bound = right
        else:
            return [-1, -1]

        return [left_bound, right_bound]
