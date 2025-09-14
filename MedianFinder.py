import heapq


class MedianFinder:
    """
    思路是这样的：

    维护两个栈： 最小栈和最大栈。


    1、 最大栈： 中位数左边偏小的部分。
    2.  最小栈： 中位数右边偏大的部分。

    每次根据数字， 如果小于最大栈里面的元素， 往最大栈里面添加
    如果大于最小栈里面的元素往最小栈添加。

    确保最大栈的里面的元素始终比最小栈多一个。
    """

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def _balance(self):
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -(heapq.heappop(self.max_heap)))

        elif len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -(heapq.heappop(self.min_heap)))

    def addNum(self, num: int) -> None:
        if not self.max_heap or -self.max_heap[0] > num:
            heapq.heappush(self.max_heap, -num)

        else:
            heapq.heappush(self.min_heap, num)

        self._balance()

    def findMedian(self) -> float:
        # if not self.max_heap:
        #     return None

        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0

        else:
            return -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
