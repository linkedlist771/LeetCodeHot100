from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        这个题的思路还是和旋转k次后的数组一样：

        因为二分这个数组后依然是一半有序， 一半部分有序， 通过判断 边界大小来判断那边有序。
        判断这个有序里面最大值是不是小于mid， 判确定最小值在哪里
        """
        l, r = 0, len(nums) - 1

        while l < r:  # 注意这里是 < 不是看， 这里和很一般的二分不同
            # l == r  的时候就是答案， 不断缩小区间， 如果是<= 则会超时。
            mid = (r - l) // 2 + l

            if nums[mid] > nums[r]:
                # 最小值在右边
                l = mid + 1

            else:
                # 最小值在左边，包括mid
                r = mid

        return nums[l]
