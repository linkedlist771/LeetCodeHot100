# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head: ListNode):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not head or not head.next:
            return head

        last = None
        # dummy = ListNode()
        # dummy.next = head
        new_head = head.next
        prev = head
        current = head.next

        while current:
            _current = current
            _next = current.next
            current.next = prev
            prev.next = _next
            if last:
                last.next = current
            # else:
            #     # 第一次交换时，更新 dummy 的连接
            #     dummy.next = current
            last = prev
            if not _next:
                break
            prev = _next
            current = prev.next

            # last = prev

        return new_head


_head = [1, 2, 3, 4]
head = ListNode()
dummy = head
for h in _head:
    head.next = ListNode(val=h)
    head = head.next

head = dummy.next
# while head:
#     print(head.val)
#     head = head.next
h = Solution().swapPairs(head)

while h:
    print(h.val)
    h = h.next

# 输出：[2,1,4,3]
