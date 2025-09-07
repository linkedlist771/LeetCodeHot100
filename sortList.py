from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        使用归并排序来完成：
        1. 每次找到链表的中间，然后拆开合并。
        2. 然后返回返回就行了。
        """
        if not head or not head.next:
            return head

        def merge(l1: Optional[ListNode], l2: Optional[ListNode]):
            # 使用dummy head来完成
            dummy = ListNode()
            current = dummy

            while l1 and l2:  # 当两者都存在
                if l1.val < l2.val:
                    current.next = l1
                    l1 = l1.next

                else:
                    current.next = l2
                    l2 = l2.next
                # 移动一下current
                current = current.next

            if l1:
                current.next = l1
            elif l2:
                current.next = l2
            return dummy.next

        # 使用快慢指针进行找到中点， 其中fast一次走两个
        # slow一次走一个，当fast到达尾巴，此时slow就是中值，拆开即可
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # 需要断开链表
        prev.next = None
        # 拆开
        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return merge(l1, l2)
