# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        维护当前需要交换的两个node和他们前面的一个node。 然后每次交换他们两个然后和前面的连起来。
        最后返回head就行了。
        """
        if not head or not head.next:  # 排除掉只有一个和没有节点的情况。
            return head

        # 保存新的头节点（原来的第二个节点）
        new_head = head.next

        prev = head
        current = head.next
        last = None

        while prev and current:  # 两个都必须存在
            # 交换
            left = prev
            right = current

            left.next = right.next
            right.next = left

            # 连接上一对
            if last:
                last.next = right

            # 更新指针
            last = left  # left 现在是这一对的第二个节点
            prev = left.next
            current = prev.next if prev else None

        return new_head  # 返回新的头节点
