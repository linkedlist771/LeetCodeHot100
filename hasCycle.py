# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """



        使用快慢指针来实现。。。。。。。
        """

        # 假设这个环有N个元素， 那么慢指针一定可以遇到快指针

        slow = head
        if slow is None:
            return False
        fast = head.next
        if fast is None:
            return False

        while slow and fast:
            if slow == fast:
                return True
            slow = slow.next
            if slow is None or fast.next is None:
                return False
            fast = fast.next.next

        return False
