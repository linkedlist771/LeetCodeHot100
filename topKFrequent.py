import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        思路是这样的：
        1. 首先统计每个num的数字频率。
        2. 把数字构建一个最小堆（最多k个元素）， 每次添加都是保证这个最小堆堆定最小。
        3. 超过k个pop元素， 最后这个堆里面剩下的就是top k的。
        """
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        heap = []

        for num, f in freq.items():
            heapq.heappush(heap, (f, num))  # 按照第一个排序
            if len(heap) > k:
                heapq.heappop(heap)
        return [i[1] for i in heap]
