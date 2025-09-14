from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        思路：中心扩散法 + 跳跃
        每个进行中心扩散法， 但是扩散的时候存储历史的每个节点的最左和最有的记录。

        满足的要求就是左边和右边的，只要是height大于等于当前的就行了， 可以扩展。
        """

        n = len(heights)
        left = [0] * n
        right = [0] * n

        # 对于0的最左边就是0
        for i in range(1, n):
            left_most = i - 1
            while left_most >= 0 and heights[left_most] >= heights[i]:  # 可以一直扩展
                left_most = left[left_most] - 1  # 多跳一个

            left[i] = left_most + 1

        right[n - 1] = n - 1
        for i in range(n - 2, -1, -1):
            right_most = i + 1
            while right_most < n and heights[right_most] >= heights[i]:  # 可以一直扩展
                right_most = right[right_most] + 1  # 多跳一个

            right[i] = right_most - 1
        # 求最大面积
        max_area = 0
        for idx, (l, r) in enumerate(zip(left, right)):
            max_area = max((r - l + 1) * heights[idx], max_area)
        return max_area

        # for idx, h in enumerate(heights):

        # 先计算left的
