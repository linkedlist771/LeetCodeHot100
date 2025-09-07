# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        思路1：
        两个值走， 一个先走n个，然后另一个两个一起走， 结束的就是倒数第n个就行了。
        """

        # 主要是不是head被删了

        fast = head
        for _ in range(n):
            fast = fast.next

        slow = head
        prev = None
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next

        # 删除slow这个位置的，也就只是把slow前面指向后面的然后删除掉前面的。
        # 已经记录了prev的
        if prev is None:
            # 怎么这就是最后一个了， 也就是说这是第一个。
            prev = slow

            slow = slow.next
            del prev
            return slow
        else:
            # 非空。
            prev.next = slow.next
            del slow

            return head
