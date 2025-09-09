class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node

        # 创建虚拟头尾节点
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        """在头部添加节点"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """删除节点"""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_head(self, node):
        """移动节点到头部"""
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """删除尾部节点"""
        tail_node = self.tail.prev
        self._remove_node(tail_node)
        return tail_node

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node:
            # 移动到头部
            self._move_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)

        if node:
            # 更新值并移动到头部
            node.value = value
            self._move_to_head(node)
        else:
            # 新增节点
            if len(self.cache) >= self.capacity:
                # 删除尾部节点
                tail = self._pop_tail()
                del self.cache[tail.key]

            new_node = DLinkedNode(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
