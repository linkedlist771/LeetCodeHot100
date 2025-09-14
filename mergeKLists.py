# Definition for singly-linked list.


from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        思路是这样的： 按中点拆分两个数组， 然后递归调用， 合并。
        """

        def merge(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode()
            head = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    dummy.next = l1
                    l1 = l1.next
                else:
                    dummy.next = l2
                    l2 = l2.next
                dummy = dummy.next
            rest = l1 or l2
            dummy.next = rest
            return head.next

        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]
        if n == 2:
            return merge(lists[0], lists[1])
        mid = n // 2

        left = lists[:mid]
        right = lists[mid:]

        left = self.mergeKLists(left)
        right = self.mergeKLists(right)
        return merge(left, right)
