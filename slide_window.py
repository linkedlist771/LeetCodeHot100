from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 我们需要维护一个单调的队列， 之类的，每次来了新的的
        # 他必须是单调的，由于我们只关心最大的。 每次移动要去掉当前哪个元素
        # 那么比那个元素小的也可以都被丢掉了？

        """
        所以思路是这样的：
        1. 维护一个单调递减双端队列， 只关系队列第一个是什么。
        2. 滑动窗口后，添加新的元素， pop掉这个队列的后面的元素，到这个元素的位置，然后添加。
        3. 然后去掉由于滑动窗口导致的去掉的索引.(注意是在当前窗口里面比较， 然后存的是索引）
        最后返回这个队列第一个元素就行了。。
        """

        n = len(nums)
        queue = deque()

        for i in range(k):
            while queue and nums[i] > nums[queue[-1]]:  # 存的是索引
                queue.pop()
            queue.append(i)  # 这个添加都是对应其最大的位置了。
        ans = [nums[queue[0]]]

        for i in range(k, n):
            # 先添加
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)  # 这个添加都是对应其最大的位置了。

            # 然后过滤掉窗口里面的元素。
            # 当前窗窗口 [i-k+1,  i]
            while queue[0] < i - k + 1:
                queue.popleft()
            ans.append(nums[queue[0]])

        return ans
