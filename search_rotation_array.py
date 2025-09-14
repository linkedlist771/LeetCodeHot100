from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        这个也是用二分解决的， 不同的是。

        但是有个特点是， 两个区间至少有一个排序好的， 排序好的条件就是
        nums[region_left] <= nums[region_right]
        然后进有序的部分里面找， 如果找到了， 那么就在里面， 如果不在
        就二分另一个部分， 继续这样的操作
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] == target:  # 找到了
                return mid

            # 进行二分查找:
            if nums[left] <= nums[mid]:
                # 怎么左边有序， 看看数值在不在里面
                if nums[left] <= target <= nums[mid]:
                    # 在这里面进行二分
                    right = mid - 1

                else:
                    # 去右边找
                    left = mid + 1
            else:
                # 右边有序
                if nums[mid] <= target <= nums[right]:
                    # 在这里面进行二分
                    left = mid + 1

                else:
                    # 去左边边找
                    right = mid - 1
        return -1
