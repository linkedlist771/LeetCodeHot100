from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        思路是这样的， 采用递归来处理， 移动k个head，然后再调用这个。
        """
        count = 0
        current = head
        while current and count < k:
            current = current.next
            count += 1

        if count >= k:
            prev = self.reverseKGroup(current, k)
        else:
            return head  # 不足k个直接返回

        # 然后翻转前k个

        current = head
        for _ in range(k):
            _next = current.next
            current.next = prev
            prev = current
            current = _next
            count -= 1

        return prev
