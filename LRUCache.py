from typing import Optional


class DLLinkedList:
    def __init__(
        self,
        key: int,
        val: int,
        prev: Optional["DLLinkedList"] = None,
        next: Optional["DLLinkedList"] = None,
    ):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        """
        LRU (Least Recently Used), 读写都算。
        需要一个哈希表和一个双向链表，
        1. 双向链表头指向最近使用的，
        2. 尾指向最后使用的。
        3. 新增的时候， 判断是否存在， 如果存在， 就修改值然后调整到链表头。
        如果不存在，则头插， 然后判断是否超了， 如果超了删除尾巴。
        3. 获取的时候， 判断这个值在不在列表里面， 如果在， 则返回， 然后
        移动这个值到链表头。

        记得double linkedlist 需要存储key 和val 方便cache删除key，
        还有呢， 删除和连接双向链表的的时候链接两次。

        然后初始化的时候把head 和 tail连接起来， 直接双向链接。


        """
        self.capacity = capacity
        self.cache = {}
        self.head = DLLinkedList(0, 0)
        self.tail = DLLinkedList(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head  # 连起来

    def _remove_node(self, node: DLLinkedList):
        if node and node.prev and node.next:
            node.prev.next = node.next

            node.next.prev = node.prev

    def _move_to_head(self, node: DLLinkedList):
        self._remove_node(node)
        head_next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = head_next
        head_next.prev = node

    def _pop_tail(self) -> DLLinkedList:
        tail = self.tail.prev
        self._remove_node(tail)
        return tail

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._move_to_head(node)
        else:
            if len(self.cache) >= self.capacity:
                tail_node = self._pop_tail()
                del self.cache[tail_node.key]  # 记得删除
            node = DLLinkedList(key=key, val=value)

            self._move_to_head(node)

            self.cache[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
