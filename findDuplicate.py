from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """

        由于包含n+1数字， 数值范围都在1,n里面， 其中一个重复。
        所以可以构建一个链表，
        其中index -> nums[index]
        而nums[index] 指向 nums[nums[index]] ...

        由于具有重复的值， 所以这个一定有环， 那么利用链表的检测环的算法就行。快慢指针

        """

        slow = fast = 0

        # 1. 找到相遇点
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] # 走两个
            if slow == fast:
                break # 一定相遇

        # 2. 找到环的入口
        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast









