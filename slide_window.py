from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        # 我们需要维护一个单调的队列， 之类的，每次来了新的的
        # 他必须是单调的，由于我们只关心最大的。 每次移动要去掉当前哪个元素
        # 那么比那个元素小的也可以都被丢掉了？
